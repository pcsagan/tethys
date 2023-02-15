"""Quick start script."""
from distutils.sysconfig import get_python_lib
from os import getcwd, path
from typing import Any, Callable, Dict

import click
from sphinx.util.osutil import ensuredir
from sphinx.util.template import SphinxRenderer

DEFAULTS: Dict[str, Any] = {}


class QuickstartRenderer(SphinxRenderer):
    """Render the template files into source files."""

    def __init__(self, templatedir: str = "") -> None:
        self.templatedir = templatedir
        super().__init__()

    def _has_custom_template(self, template_name: str) -> bool:
        """Check if custom template file exists.

        Note: Please don't use this function from extensions.
              It will be removed in the future without deprecation period.
        """
        template = path.join(self.templatedir, path.basename(template_name))
        return bool(self.templatedir) and path.exists(template)

    def render(self, template_name: str, context: dict[str, Any]) -> str:
        """Return the rendered text from the template.

        Args:
            template_name (str): The template file name
            context (dict[str, Any]): The data used during rendering

        Returns:
            str: Rendered text
        """
        if self._has_custom_template(template_name):
            custom_template = path.join(self.templatedir, path.basename(template_name))
            return self.render_from_file(custom_template, context)
        else:
            return super().render(template_name, context)


def default_to(name: str) -> Callable:
    """Default to the value of the specified parameter.

    Args:
        name (str): The name of the parameter to use as a default value

    Returns:
        Callable: Callback that returns either truthy value or the default
    """
    return lambda context, param, value: value if value else context.params[name]


@click.command()
@click.option("--project", prompt="Enter the project name", help="Project name")
@click.option("--pypi", callback=default_to("project"), help="PyPI name")
@click.option("--description", prompt="Enter the project description", help="Project description")
@click.option("--author-name", prompt="Enter the author name", help="Author name")
@click.option("--author-email", prompt="Enter the author e-mail", help="Author e-mail")
@click.option("--repo", prompt="Enter the Github repository", help="Github repository")
@click.option("--quiet", is_flag=True, help="Silent when set")
@click.argument("destination")
def main(project, pypi, description, author_name, author_email, repo, quiet, destination):
    """Tethys quick start script."""
    # get the path to the installed templates in site-packages
    template_dir = path.join(get_python_lib(), "tethys", "templates", "quickstart")

    # get the full path to the output directory
    destination_dir = path.join(getcwd(), destination)
    ensuredir(destination_dir)

    data = {
        "project": project,
        "pypi": pypi,
        "description": description,
        "author_name": author_name,
        "author_email": author_email,
        "repo": repo
    }
    template = QuickstartRenderer(template_dir)

    def write_template(
        template_name: str, destination_rel_path: str, data: dict
    ) -> None:
        template_path = path.join(template_dir, template_name)
        output_path = path.join(destination_dir, destination_rel_path)
        with open(template_path, encoding="utf-8") as f:
            contents = f.read()
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(template.render_string(contents, data))

    write_template("pyproject.toml_t", "pyproject.toml", data)
    write_template("tox.ini_t", "tox.ini", data)
    write_template("SECURITY.md_t", "SECURITY.md", data)
