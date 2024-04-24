# TODO trying to find the best way to run the budget CLI app
# TODO perhaps making the command -> make env <-
# .Phony budget: venv/bin/activate
# 	source venv/bin/activate

venv/bin/activate:
	python3 -m venv budgetenv
	./budgetenv/bin/pip3 install typer
