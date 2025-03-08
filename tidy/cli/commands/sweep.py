import importlib
import json
import pkgutil
from pathlib import Path
import sys

import click

from tidy.cli.options import OptionEatAll
from tidy.config.tidy_config import TidyConfig
from tidy.manifest import ManifestWrapper
from tidy.sweeps.base import CheckResult, CheckStatus

DEFAULT_CHECKS_PATH = importlib.resources.files(importlib.import_module("tidy.sweeps"))


@click.command()
@click.option(
    "--manifest-path",
    help="Path to the dbt manifest file.",
)
@click.option(
    "--max-details",
    "-md",
    default=5,
    show_default=True,
    help="Maximum number of details to display per result.",
)
@click.option(
    "--output-failures",
    "-o",
    type=click.Path(path_type=Path),
    help="Path to save failures in JSON format. If not specified, no file is written.",
)
@click.option(
    "--sweeps",
    "-s",
    cls=OptionEatAll,
    type=tuple,
    help="List of check names to run. If not specified, all checks will be run.",
)
@click.pass_context
def sweep(
    ctx,
    manifest_path,
    max_details,
    output_failures,
    sweeps,
):
    _set_context()
    
    click.secho("Sweeping...", fg="cyan", bold=True)
    results = _discover_and_run_checks()

    failures = []

    for result in results:
        status_color = {
            CheckStatus.PASS: "green",
            CheckStatus.FAIL: "red",
            CheckStatus.WARNING: "yellow",
        }.get(result.status.value, "white")

        click.secho(f"\n{result.name}", fg="cyan", bold=True)
        click.secho(f"Status: {result.status.value}", fg=status_color)
        if result.resolution:
            click.secho(f"Resolution: {result.resolution}", fg="magenta")

        if result.nodes:
            click.secho("Nodes:", fg="blue")
            for detail in result.nodes[:max_details]:
                click.echo(f"  - {detail}")

            if len(result.nodes) > max_details:
                click.secho(
                    f"  ...and {len(result.nodes) - max_details} more", fg="yellow"
                )

        if result.status.value == CheckStatus.FAIL:
            failures.append(
                {
                    "check_name": result.name,
                    "status": result.status.value,
                    "nodes": result.nodes,
                    "resolution": result.resolution,
                }
            )

    if failures:
        _handle_failure(failures=failures)


@click.pass_context
def _set_context(ctx):
    ctx.ensure_object(dict)

    config = TidyConfig()

    if ctx.params["sweeps"]:
        config.mode = "include"
        config.sweeps = list(ctx.params["sweeps"])

    if ctx.params["manifest_path"]:
        config.manifest_path = ctx.params["manifest_path"]
    
    ctx.obj["tidy_config"] = config
    
    ctx.obj["manifest"] = ManifestWrapper.load(config.manifest_path)


@click.pass_context
def _discover_and_run_checks(ctx):
    """Discovers and runs all available checks from both built-in and user-defined sources."""
    results = []
    
    results.extend(_load_checks_from_package(str(DEFAULT_CHECKS_PATH), "tidy.sweeps."))
    results.extend(_load_checks_from_directory(ctx.obj["tidy_config"].custom_sweeps_path))

    return results


def _load_checks_from_package(base_path: str, package_prefix: str):
    """Dynamically loads and runs checks from a package."""
    results = []

    for _, module_name, ispkg in pkgutil.walk_packages([base_path], package_prefix):
        if ispkg:
            continue

        try:
            module = importlib.import_module(module_name)
        except ImportError as e:
            print(f"Warning: Failed to import {module_name}: {e}")
            continue

        results.extend(_run_checks_from_module(module))

    return results


def _load_checks_from_directory(directory: Path):
    """Dynamically loads and runs checks from a directory of Python files."""
    results = []

    if not directory.exists():
        return results

    sys.path.insert(0, str(directory))

    for check_file in directory.rglob("*.py"):
        
        module_name = (
            check_file.relative_to(directory)
            .with_suffix("")
            .as_posix()
            .replace("/", ".")
        )
        
        try:
            module = _import_module_from_path(module_name, check_file)
        except ImportError as e:
            print(f"Warning: Failed to import {module_name}: {e}")
            continue

        results.extend(_run_checks_from_module(module))

    return results


@click.pass_context
def _run_checks_from_module(ctx, module):
    """Runs all checks defined in a module."""
    results = []
    tidy_config = ctx.obj["tidy_config"]

    for attr_name in dir(module):
        attr = getattr(module, attr_name)

        if callable(attr) and getattr(attr, "__is_sweep__", False):
            sweep = getattr(attr, "__name__", attr_name)

            if tidy_config.sweeps:
                if tidy_config.mode == "include":
                    if sweep not in tidy_config.sweeps:
                        continue
                elif tidy_config.mode == "exclude":
                    if sweep in tidy_config.sweeps:
                        continue

            check_result = attr(ctx.obj["manifest"])
            if isinstance(check_result, CheckResult):
                results.append(check_result)

    return results


def _import_module_from_path(module_name, path):
    """Dynamically import a module from a given file path."""
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@click.pass_context
def _handle_failure(ctx, failures: list[dict]):
    output_failures_path = ctx.params["output_failures"]
    if output_failures_path:
        if output_failures_path.is_dir():
            output_file = output_failures_path / "tidy_failures.json"
        else:
            output_file = output_failures_path

        with output_file.open("w") as f:
            json.dump(failures, f, indent=4)

    click.secho("\nSome checks failed!", fg="red", bold=True)
    sys.exit(1)
