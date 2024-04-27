# Entry point for the App.

# Third Party imports
import typer
from typing_extensions import Annotated
from typing import Optional

from datetime import date

# Local imports
from db_manager import db_print_table

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

# TODO need a commands to edit transactions

# TODO the goal of this command is too display only the data the user wishes to see.
#   Perhaps it can take args such as: month range.
@app.command()
def display() -> None:
    db_print_table()
    today: date = date.today()
    print("Date is: ", today)
    ord: int = today.toordinal()
    print("The int value: ", ord)
    d: date = date.fromordinal(ord)
    print("From ordinal is: ", d)



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
