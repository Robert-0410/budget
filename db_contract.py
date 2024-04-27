# Holds literals used for sqlite operations

DB_DIR = './.database'
DB_PATH = f'{DB_DIR}/ledger.db'

# Table Name
LEDGER = 'ledger'

# Columns
DIRECTION = 'direction'
AMOUNT = 'amount'
REASON = 'reason'
DATE ='date'
BEFORE = 'before'
BALANCE = 'balance'

# Directions Values
INCOMING = 1
OUTGOING = -1

CREATE_LEDGER_TABLE = f"CREATE TABLE IF NOT EXISTS {LEDGER} ( "\
                            f"{DIRECTION} INTEGER DEFAULT 0, "\
                            f"{AMOUNT} FLOAT DEFAULT 0.0, "\
                            f"{REASON} TEXT DEFAULT Unknown, "\
                            f"{DATE} INTEGER DEFAULT 0, "\
                            f"{BEFORE} FLOAT NOT NULL, "\
                            f"{BALANCE} FLOAT NOT NULL);"

INSERT_TRANSACTION = f'INSERT INTO {LEDGER} VALUES(?, ?, ?, ?, ?, ?)'

SELECT_LAST_TRANSACTION = f'SELECT {BALANCE} FROM {LEDGER} ORDER BY rowid DESC LIMIT 1;'

def check_str() -> None:
    print(INSERT_TRANSACTION)
    print(DB_DIR)
    print(DB_PATH)
    print(CREATE_LEDGER_TABLE)



