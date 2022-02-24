import json
import typer
from omm_monk_cli.icx import Icx

app = typer.Typer()
icx = Icx()


@app.command()
def hello():
    typer.echo("Hello")


@app.command()
def submit_token_transfer(value: int, token_contract: str, to_address: str):
    """
    Calls the submitTransaction method.
    """
    if token_contract[:2] != "cx":
        try:
            token_contract = icx.TICKER_TO_CONTRACT[token_contract]
        except KeyError as e:
            typer.echo(f"ERROR: {token_contract} is not a supported token.")
            raise typer.Exit()
    exa = icx.CONTRACT_TO_EXA[token_contract]
    params = {
        "_destination": token_contract,
        "_method": "transfer",
        "_params": json.dumps(
            [
                {
                    "name": "_to",
                    "type": "Address",
                    "value": to_address,
                },
                {"name": "_value", "type": "int", "value": f"{value * 10**exa}"},
            ]
        ),
    }

    tx_hash = icx.call_tx(icx.MONK_MULTISIG_CONTRACT, "submitTransaction", params)
    typer.echo(tx_hash)


@app.command()
def confirm_transaction(transaction_id: int):
    """
    Calls the confirmTransaction method.
    """
    tx_hash = icx.call_tx(
        icx.MONK_MULTISIG_CONTRACT,
        "confirmTransaction",
        {"_transactionId": transaction_id},
    )
    typer.echo(tx_hash)
