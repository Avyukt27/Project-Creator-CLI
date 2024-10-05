#!/usr/bin/env python3
"""Main Script"""

import typer
from rich.console import Console

import cli
import ui

console = Console()
app = typer.Typer()


@app.command("ui")
def ui_app():
    """Runs the UI"""
    ui.create()


@app.command("cli")
def cli_app():
    """Runs the CLI"""
    cli.create()


if __name__ == "__main__":
    app()
