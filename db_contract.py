
from enum import Enum

# Holds literals used for sqlite operations

DB_DIR = './.database'
DB_PATH = f'{DB_DIR}/ledger.db'

# Table Name
LEDGER = 'ledger'

# Columns
class LedgerColumns(Enum):
    direction = 0
    amount = 1
    reason = 2
    date = 3
    before = 4
    balance = 5

# Directions Values
INCOMING = 1
OUTGOING = -1

CREATE_LEDGER_TABLE = f"CREATE TABLE IF NOT EXISTS {LEDGER} ( "\
                            f"{LedgerColumns.direction.name} INTEGER DEFAULT 0, "\
                            f"{LedgerColumns.amount.name} FLOAT DEFAULT 0.0, "\
                            f"{LedgerColumns.reason.name} TEXT DEFAULT Unknown, "\
                            f"{LedgerColumns.date.name} INTEGER DEFAULT 0, "\
                            f"{LedgerColumns.before.name} FLOAT NOT NULL, "\
                            f"{LedgerColumns.balance.name} FLOAT NOT NULL);"

INSERT_TRANSACTION = f'INSERT INTO {LEDGER} VALUES(?, ?, ?, ?, ?, ?)'

SELECT_LAST_TRANSACTION = f'SELECT {LedgerColumns.balance.name} FROM {LEDGER} ORDER BY rowid DESC LIMIT 1;'

def check_str() -> None:
    print(INSERT_TRANSACTION)
    print(DB_DIR)
    print(DB_PATH)
    print(CREATE_LEDGER_TABLE)



