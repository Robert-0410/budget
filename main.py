import typer

app = typer.Typer()

@app.command()
def incoming(amount: int):
    print(f"Added: ${amount}")

@app.command()
def outgoing(amount: int):
    print(f"Subtracted: ${amount}")


if __name__ == '__main__':
    app()
