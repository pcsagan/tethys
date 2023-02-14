"""Command Line Interface."""
import click


@click.group()
@click.version_option()
@click.option(
    "--debug", default=False, is_flag=True, help="Run the command in debug mode."
)
@click.pass_context
def main(ctx, debug):
    """Tethys command line interface."""
    ctx.ensure_object(dict)
    ctx.obj = {"debug": debug}


@main.command()
@click.pass_context
def foo(ctx):
    """Print the word 'bar' in red if debug is true, or green if debug is false."""
    color = "red" if ctx.obj["debug"] else "green"
    click.secho("bar", fg=color)


@main.command()
@click.pass_context
def data(ctx):
    """Print the shared context data to the screen."""
    click.echo(ctx.obj)
