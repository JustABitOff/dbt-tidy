import importlib
import pkgutil
import pathlib
import sys

import click

from tidy.manifest.v12.manifest import parse_manifest
from tidy.sweeps.base import CheckResult

DEFAULT_CHECKS_PATH = pathlib.Path(__file__).parent.parent / "sweeps"
USER_CHECKS_PATH = pathlib.Path.cwd() / "tidy_custom"


def discover_and_run_checks(manifest, check_names=None):
    results = []

    if USER_CHECKS_PATH.exists():
        sys.path.insert(0, str(USER_CHECKS_PATH))

    for checks_path, checks_pkg_name in [
        (DEFAULT_CHECKS_PATH, "tidy.sweeps"),
        (USER_CHECKS_PATH, "tidy_custom"),
    ]:
        if not checks_path.exists():
            continue

        for finder, name, ispkg in pkgutil.walk_packages(
            [str(checks_path)], f"{checks_pkg_name}."
        ):
            if ispkg:
                continue

            module = importlib.import_module(name)

            check_name = name.split(".")[-1]

            if check_names and check_name not in check_names:
                continue

            if hasattr(module, "sweep"):
                check_result = module.sweep(manifest)
                if isinstance(check_result, CheckResult):
                    results.append(check_result)

    return results


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--manifest-path",
    default="target/manifest.json",
    show_default=True,
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
    "--sweeps",
    "-s",
    multiple=True,
    help="List of check names to run. If not specified, all checks will be run.",
)
def sweep(
    manifest_path,
    max_details,
    sweeps,
):
    manifest = parse_manifest(manifest_path)
    click.secho("Sweeping...", fg="cyan", bold=True)
    results = discover_and_run_checks(manifest, sweeps)

    for result in results:
        status_color = {"pass": "green", "fail": "red", "warning": "yellow"}.get(
            result.status.value, "white"
        )

        click.secho(f"\n{result.name}", fg="cyan", bold=True)
        click.secho(f"Status: {result.status.value}", fg=status_color)

        if result.nodes:
            click.secho("Nodes:", fg="blue")
            for detail in result.nodes[:max_details]:
                click.echo(f"  - {detail}")

            if len(result.nodes) > max_details:
                click.secho(
                    f"  ...and {len(result.nodes) - max_details} more", fg="yellow"
                )


if __name__ == "__main__":
    cli()
