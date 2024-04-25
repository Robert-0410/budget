# Holds literals used for sqlite operations

DB_DIR = './.database'
DB_PATH = f'{DB_DIR}/ledger.db'

# Table Name
LEDGER = 'ledger'

# Columns
UID = 'uid' # might not need this because of the ROWID default behavior of SQLite.
DIRECTION = 'direction'
AMOUNT = 'amount'
FOR = 'for'
DATE ='date'
BEFORE = 'before'
AFTER = 'after'

CREATE_LEDGER_TABLE = f"CREATE TABLE IF NOT EXISTS {LEDGER} ( "\
                            f"{DIRECTION} INTEGER DEFAULT 0, "\
                            f"{AMOUNT} FLOAT DEFAULT 0.0, "\
                            f"{FOR} TEXT DEFAULT Unknown, "\
                            f"{DATE} INTEGER DEFAULT 0, "\
                            f"{BEFORE} FLOAT NOT NULL, "\
                            f"{AFTER} FLOAT NOT NULL);"

INSERT_TRANSACTION = f'INSERT INTO {LEDGER} VALUES(?, ?, ?, ?, ?, ?)'



def check_str() -> None:
    print(INSERT_TRANSACTION)
    print(DB_DIR)
    print(DB_PATH)
    print(CREATE_LEDGER_TABLE)



