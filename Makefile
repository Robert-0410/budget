# TODO trying to find the best way to run the budget CLI app
# TODO perhaps making the command -> make env <-
# .Phony budget: venv/bin/activate
# 	source venv/bin/activate

db: budgetenv/bin/activate
	python3 db_manager.py

# TODO Should requirements.txt be used???
budgetenv/bin/activate:
	python3 -m venv budgetenv
	./budgetenv/bin/pip3 install typer


# env: budgetenv/bin/activate
# 	source budgetenv/bin/activate
#
# .PHONY: env
.PHONY: db
