# Entry point for the App.

# Third Party imports
import typer
from typing_extensions import Annotated
from typing import Optional

# Local imports
import db_contract

app = typer.Typer()

#                       float  str str
# TODO potentail args : amount for date
#   date will be optional and will get the datetime from the system instead
@app.command()
def add(amount: float) -> None:
    print(f"Added: ${amount}")

@app.command()
def sub(amount: float) -> None:
    print(f"Subtracted: ${amount}")


# Using the following as a way to experiment with typer's features
@app.command()
def test(arg1: Annotated[Optional[str], typer.Argument()] = None,
         arg2: Annotated[Optional[str], typer.Argument()] = None) -> None:
    if arg1 is None:
        print("No Args passed")
    else:
        print(f"The Arg passed! -> {arg1} with second as {arg2}")


if __name__ == '__main__':
    app()
