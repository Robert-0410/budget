
# Used to conduct all database related computation.

from datetime import date
from decimal import Decimal
import os
import sqlite3

# Local imports
import db_contract

# [[ Admin database management

# TODO Need to learn how to do proper python documentation.

# Creates the SQLite database and the tables used within the application.
def db_create() -> None:
    if not os.path.exists(db_contract.DB_DIR):
        os.makedirs(db_contract.DB_DIR)
        today: date = date.today()
        conn = sqlite3.connect(db_contract.DB_PATH)
        cur = conn.cursor()
        cur.execute(db_contract.CREATE_LEDGER_TABLE)
        # Init balance to $0.0
        cur.execute(db_contract.INSERT_TRANSACTION, (db_contract.INCOMING, 0.0, 'Budget Created', today.toordinal(), 0.0, 0.0))
        conn.commit()
        cur.close()
        conn.close()

def db_print_table() -> None:
    conn = sqlite3.connect(db_contract.DB_PATH)
    cur = conn.cursor()
    for row in cur.execute(f"SELECT * FROM {db_contract.LEDGER}"):
        print(row)
    cur.close()
    conn.close()

# Admin database management ]]

# [[ Runtime functions

def db_get_transactions() -> list[tuple]:
    output: list[tuple] = []
    conn = sqlite3.connect(db_contract.DB_PATH)
    cur = conn.cursor()
    for row in cur.execute(f"SELECT * FROM {db_contract.LEDGER}"):
        output.append(row)
    cur.close()
    conn.close()
    return output

def db_insert_transaction(direction: int,
                          amount: float,
                          reason: str,
                          date: int) -> float:
    conn = sqlite3.connect(db_contract.DB_PATH)
    cur = conn.cursor()
    res = cur.execute(db_contract.SELECT_LAST_TRANSACTION)
    prev_balance = res.fetchone()[0]
    d_balance: Decimal = Decimal(prev_balance)
    new_balance: Decimal
    if direction is db_contract.INCOMING:
        new_balance = d_balance + Decimal(amount)
    else:
        new_balance = d_balance - Decimal(amount)
    output = float(round(new_balance, 2))
    cur.execute(db_contract.INSERT_TRANSACTION, (direction, amount, reason, date, prev_balance, output))
    conn.commit()
    cur.close()
    conn.close()
    return output

# Runtime functions ]]

if __name__ == '__main__':
    db_create()

