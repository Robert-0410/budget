
# Used to conduct all database related computation.

from datetime import date
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

def db_insert_transaction(direction: int,
                          amount: float,
                          reason: str,
                          date: int) -> float:
    conn = sqlite3.connect(db_contract.DB_PATH)
    cur = conn.cursor()
    res = cur.execute(db_contract.SELECT_LAST_TRANSACTION)
    last_balance: float = res.fetchone()[0]
    new_balance: float
    print("The last balance: ", last_balance)
    if direction is db_contract.INCOMING:
        new_balance = last_balance + amount
    else:
        new_balance = last_balance - amount
    cur.execute(db_contract.INSERT_TRANSACTION, (direction, amount, reason, date, last_balance, new_balance))
    conn.commit()
    cur.close()
    conn.close()
    return new_balance

def db_print_table() -> None:
    conn = sqlite3.connect(db_contract.DB_PATH)
    cur = conn.cursor()
    for row in cur.execute(f"SELECT * FROM {db_contract.LEDGER}"):
        print(row)
    res = cur.execute(f"SELECT rowid FROM {db_contract.LEDGER}")
    print(res.fetchall())
    cur.close()
    conn.close()

# Admin database management ]]

# [[ Runtime functions
# Runtime functions ]]

if __name__ == '__main__':
    db_create()

