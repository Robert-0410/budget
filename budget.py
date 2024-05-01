# Entry point for the App.

# Third Party imports
import typer
from typing_extensions import Annotated
from typing import Optional
from rich import print
from rich.console import Console
from rich.table import Table

from datetime import datetime, date

# Local imports
from db_contract import LedgerColumns, INCOMING, OUTGOING
from db_manager import db_get_transactions, db_insert_transaction

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
    print(f"The new balance: $[bold green]{balance}[/bold green]")


@app.command()
def sub(amount: Annotated[float, typer.Argument()],
        reason: Annotated[str, typer.Argument()],
        date: Annotated[Optional[datetime], typer.Argument()] = datetime.today()) -> None:
    balance: float = db_insert_transaction(OUTGOING,
                                           amount,
                                           reason,
                                           date.toordinal())
    print(f"The new balance: $[bold red]{balance}[/bold red]")

# TODO need a commands to edit transactions

# TODO the goal of this command is too display only the data the user wishes to see.
#   Perhaps it can take args such as: month range.
@app.command()
def display() -> None:
    transactions: list[tuple] = db_get_transactions()
    table = Table(title='Ledger', show_lines=True)
    table.add_column(str.upper(LedgerColumns.direction.name), style='cyan', justify='center')
    table.add_column(str.upper(LedgerColumns.amount.name), justify='left', style='green')
    table.add_column(str.upper(LedgerColumns.reason.name), style='cyan')
    table.add_column(str.upper(LedgerColumns.date.name), style='green')
    table.add_column(str.upper(LedgerColumns.before.name), style='cyan', justify='left')
    table.add_column(str.upper(LedgerColumns.balance.name), style='green', justify='left')
    for row in transactions:
        direction, amount, reason, when, before, balance = row
        d: str
        if direction < 0:
            d = '-'
        else:
            d = '+'
        day = date.fromordinal(when)
        table.add_row(d, f"${amount}", reason, str(day), f"${before}", f"${balance}")
    print(table)

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
