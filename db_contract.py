# Holds literals used for sqlite operations

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

CREATE_LEDGER_TABLE = f"CREATE TABLE {LEDGER} ( "\
                            f"{DIRECTION} INTEGER DEFAULT 0, "\
                            f"{AMOUNT} FLOAT DEFAULT 0.0, "\
                            f"{FOR} TEXT DEFAULT Unknown, "\
                            f"{DATE} INTEGER DEFAULT 0, "\
                            f"{BEFORE} FLOAT NOT NULL, "\
                            f"{AFTER} FLOAT NOT NULL);"\

def check_str() -> None:
    print(CREATE_LEDGER_TABLE)





