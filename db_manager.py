
# Used to conduct all database related computation.

from datetime import date
import os
import sqlite3

# Local imports
import db_contract

# [[ Admin database management

# Creates the SQLite database and the tables used within the application.
def db_create() -> None:
    if not os.path.exists(db_contract.DB_DIR):
        os.makedirs(db_contract.DB_DIR)
        today: date = date.today()
        conn = sqlite3.connect(db_contract.DB_PATH)
        cur = conn.cursor()
        cur.execute(db_contract.CREATE_LEDGER_TABLE)
        # Init balance to $0.0
        cur.execute(db_contract.INSERT_TRANSACTION, (1, 0.0, 'Initial', today.toordinal(), 0.0, 0.0))
        conn.commit()
        cur.close()
        conn.close()

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

