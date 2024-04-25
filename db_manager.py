
# Used to conduct all database related computation.

import os
import sqlite3

# Local imports
import db_contract

# [[ Admin database management

# Creates the SQLite database and the tables used within the application.
def db_create() -> None:
    if not os.path.exists(db_contract.DB_DIR):
        os.makedirs(db_contract.DB_DIR)
        conn = sqlite3.connect(db_contract.DB_PATH)
        cur = conn.cursor()
        cur.execute(db_contract.CREATE_LEDGER_TABLE)
        # Init balance to $0.0
        # TODO this needs to get todays date, instead of passing 0
        cur.execute(db_contract.INSERT_TRANSACTION, (1, 0.0, 'Initial', 0, 0.0, 0.0))
        cur.close()
        conn.close()

def db_print_table() -> None:
    print('Trying to print the Table')
    conn = sqlite3.connect(db_contract.DB_PATH)
    cur = conn.cursor()
    for row in cur.execute(f"SELECT * FROM {db_contract.LEDGER}"):
        print(row)
    cur.close()
    conn.close()
# Admin database management ]]

# [[ Runtime functions
# Runtime functions ]]

if __name__ == '__main__':
    db_print_table()
    # db_create()

