# Entry point for the App.

# Third Party imports
import typer
import sqlite3

# Local imports
import db_contract

app = typer.Typer()

@app.command()
def incoming(amount: float) -> None:
    print(f"Added: ${amount}")

@app.command()
def outgoing(amount: float) -> None:
    print(f"Subtracted: ${amount}")


if __name__ == '__main__':
    app()
