"""Handles the creation of folders for the project"""

import os
import subprocess
from time import sleep

from InquirerPy import inquirer
from rich.console import Console
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn

console: Console = Console()


def run_language(language: str, dir_name: str):
    """Creates the project using the given language

    Args:
        language (str): The language for the project
        dir_name (str): The directory where the project is located
    """
    match language.lower():
        case "python":
            handle_python()
        case "javascript/typescript":
            handle_js_ts(dir_name)
        case "java":
            handle_java()


def handle_python():
    """Handles creation of a python project"""
    create_venv: bool = inquirer.confirm(
        "Create Virtual Environment?", default=False
    ).execute()
    if create_venv:
        create_virtualenv(".venv")
    console.print("[green3 bold]Done[/green3 bold] :heavy_check_mark:")


def handle_js_ts(dir_name: str):
    """Handles creation of a JavaScript/TypeScript project

    Args:
        dir_name: The directory where the project is located
    """
    os.chdir("..")
    os.rmdir(dir_name)
    subprocess.run(
        f"npm create vite@latest {dir_name}", shell=True, text=True, check=True
    )
    console.print("[green4]Done[/green4] :heavy_check_mark:")


def handle_java():
    """Handles creation of Java project"""
    with open("main.java", "w", encoding="utf-8") as file:
        file.write("public class main {\n")
        file.write("\t\n")
        file.write("}")


def create_virtualenv(env_name: str):
    """Creates a virtual environment for python

    Args:
        env_name (str): The name of the virtual environment
    """
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    ) as progress:
        # Start a task for progress tracking
        task = progress.add_task(
            f"[cyan]Creating virtual environment '{env_name}'...", total=100
        )

        # Run the command to create a virtual environment using subprocess
        process = subprocess.Popen(
            ["python", "-m", "venv", env_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        # Read the process output in real-time
        while process.poll() is None:
            progress.update(task, advance=5)
            sleep(0.5)

        progress.update(task, completed=100)
