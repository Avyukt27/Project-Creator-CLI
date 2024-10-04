"""Main Script"""

# from sys import argv
from enum import Enum

import typer
from rich.console import Console
from typing_extensions import Annotated


class Mode(str, Enum):
    ui = "ui"
    cli = "cli"


console = Console()


def main(mode: Annotated[Mode, typer.Argument(help="The mode for preject creation")]):
    """Starts project creation

    Args:
        mode (str): The mode for project creation.
    """
    console.print(mode)


if __name__ == "__main__":
    typer.run(main)
