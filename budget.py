# Entry point for the App.

# Third Party imports
import typer
from typing_extensions import Annotated
from typing import Optional

from datetime import datetime

# Local imports
from db_contract import INCOMING, OUTGOING
from db_manager import db_print_table, db_insert_transaction

app = typer.Typer()

# TODO add optional date argument
@app.command()
def add(amount: Annotated[float, typer.Argument()],
        reason: Annotated[str, typer.Argument()],
        date: Annotated[Optional[datetime], typer.Argument()] = datetime.today()) -> None:
    balance: float = db_insert_transaction(INCOMING,
                                           amount,
                                           reason,
                                           date.toordinal())
    print("The new balance: $", balance)


@app.command()
def sub(amount: float) -> None:
    print(f"Subtracted: ${amount}")

# TODO need a commands to edit transactions

# TODO the goal of this command is too display only the data the user wishes to see.
#   Perhaps it can take args such as: month range.
@app.command()
def display() -> None:
    print('Direction, Amount, Reason, Date, Before, Balance')
    db_print_table()

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
