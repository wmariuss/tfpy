import click

from tfpy.changes import TerraConfigs
from tfpy.common import TerraCommon

# Init class
tf_common = TerraCommon()
tf_configs = TerraConfigs()


@click.group()
@click.version_option()
def cli():
    """
    Check and apply changes in all dirs
    """


@cli.command(help="Initialize a working directory")
def init() -> str:
    """
    Init
    """
    return tf_configs.execute_terraform_tasks(terraform="init")


@cli.command(help="Show execution plan")
def show() -> str:
    """
    Show
    """
    return tf_configs.execute_terraform_tasks(terraform="show")


@cli.command(help="Builds or change infrastructure")
def apply() -> str:
    """
    Apply
    """
    return tf_configs.execute_terraform_tasks(terraform="apply")
