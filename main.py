from InquirerPy import inquirer
from rich.console import Console
import typer
import os
from pathlib import Path

cwd = Path.cwd()
console = Console()


def new_dropdown(name: str, options: list[str]):
    return inquirer.select(name, options).execute()


def create():
    choice = new_dropdown("Test", ["test", "Test", "rw"])
    os.mkdir(os.path.join(str(cwd), choice))


if __name__ == "__main__":
    typer.run(create)
