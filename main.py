import time
from InquirerPy import inquirer
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
import typer
import os
import subprocess

cwd: str = os.getcwd()
console: Console = Console()


def new_dropdown(name: str, options: list[str]):
    return inquirer.select(name, options).execute()


def run_language(language: str, dir_name: str):
    match language.lower():
        case "python":
            create_venv: bool = inquirer.confirm(
                "Create Virtual Environment?", default=False
            ).execute()
            if create_venv:
                create_virtualenv("venv")
            console.print("[green3 bold]Done[/green3 bold] :heavy_check_mark:")
        case "javascript/typescript":
            os.chdir("..")
            os.rmdir(dir_name)
            subprocess.run(
                f"npm create vite@latest {dir_name}", shell=True, text=True
            )
            console.print("[green4]Done[/green4] :heavy_check_mark:")


def create_virtualenv(env_name: str):
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
            [f"python", "-m", "venv", env_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Read the process output in real-time
        while process.poll() is None:
            progress.update(task, advance=5)
            time.sleep(0.5)

        progress.update(task, completed=100)


def create():
    language: str = new_dropdown(
        "Pick a language", ["Python", "Javascript/Typescript"])
    choice: str = new_dropdown("Test", ["test", "Test", "rw"])
    dir_name: str = choice
    extra_num: int = 0

    while True:
        try:
            os.mkdir(os.path.join(cwd, dir_name))
            break
        except FileExistsError:
            dir_name = choice
            extra_num += 1
            dir_name += str(extra_num)

    os.chdir(choice)
    run_language(language, dir_name)


if __name__ == "__main__":
    typer.run(create)
