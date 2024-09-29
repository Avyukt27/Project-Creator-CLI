import typer
from InquirerPy import inquirer
from rich.console import Console

app = typer.Typer()
console = Console()


def new_dropdown(name: str, options: list[str]):
    return inquirer.select(name, options).execute()


@app.command("create")
def create():
    choice = new_dropdown("Test", ["test", "Test", "rw"])
    console.print(
        f"[green]You Selected:[/green] [bold magenta]{choice}[/bold magenta]"
    )


if __name__ == "__main__":
    app()
