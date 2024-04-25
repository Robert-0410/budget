#
# TODO trying to find the best way to run the budget CLI app
#	Need to learn how to launch with pip???


db : venv deps
	python3 db_manager.py

# TODO Should requirements.txt be used???
deps : venv
	venv/bin/pip3 install typer

venv :
	python3 -m venv venv

.PHONY : clean deps start
clean :
	rm -rf .database/ venv/

