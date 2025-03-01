import importlib
import pkgutil

import click

from tidy.sweeps import __name__ as checks_pkg_name
from tidy.sweeps import __path__ as checks_pkg_path
from tidy.manifest.v12.manifest import parse_manifest
from tidy.sweeps.base import CheckResult


def discover_and_run_checks(manifest, check_names=None):
    results = []

    for finder, name, ispkg in pkgutil.walk_packages(
        checks_pkg_path, checks_pkg_name + "."
    ):
        if not ispkg:
            module = importlib.import_module(name)

            if hasattr(module, "sweep"):
                if check_names and name.split(".")[-1] not in check_names:
                    continue

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
