"""CLI for Project Creator"""

import os

import typer
from InquirerPy import inquirer

import handler


def create():
    """Creates a new project"""
    language: str = inquirer.select(
        "Pick a language", ["Python", "Javascript/Typescript", "Java"]
    ).execute()
    project_name: str = inquirer.text("Enter Project Name").execute()
    dir_name: str = project_name
    extra_num: int = 0

    while True:
        try:
            os.mkdir(os.path.join(os.getcwd(), dir_name))
            break
        except FileExistsError:
            dir_name = project_name
            extra_num += 1
            dir_name += str(extra_num)

    os.chdir(dir_name)
    handler.run_language(language, dir_name)


if __name__ == "__main__":
    typer.run(create)
