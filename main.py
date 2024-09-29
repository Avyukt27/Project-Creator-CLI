from InquirerPy import inquirer
from rich.console import Console
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
            print("Python!")
        case "javascript/typescript":
            os.chdir("..")
            os.rmdir(dir_name)
            subprocess.run(f"npm create vite@latest {dir_name}", shell=True, text=True)
            print("Done")
                    


def create():
    language: str = new_dropdown("Pick a language", ["Python", "Javascript/Typescript"])
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
