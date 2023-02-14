"""Quick start script."""
import click


@click.group()
@click.version_option()
@click.pass_context
def main(ctx, debug):
    """Tethys quick start script."""
    ctx.ensure_object(dict)
    ctx.obj = {"debug": debug}

