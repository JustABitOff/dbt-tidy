import click

from tidy.cli.commands.sweep import sweep


@click.group()
def cli():
    pass


cli.add_command(sweep)

if __name__ == "__main__":
    cli()
