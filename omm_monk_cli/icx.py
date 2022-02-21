import os
import typer
from iconsdk.exception import JSONRPCException
from iconsdk.icon_service import IconService
from iconsdk.builder.call_builder import CallBuilder
from iconsdk.providers.http_provider import HTTPProvider
from iconsdk.wallet.wallet import KeyWallet
from iconsdk.builder.transaction_builder import CallTransactionBuilder
from iconsdk.signed_transaction import SignedTransaction
from dotenv import load_dotenv
from time import sleep

load_dotenv()


class Icx:

    ICON_SERVICE = IconService(HTTPProvider("https://ctz.solidwallet.io", 3))

    WALLET_PK = os.getenv("WALLET_PK")
    WALLET = KeyWallet.load(bytes.fromhex(WALLET_PK))
    WALLET_ADDRESS = WALLET.get_address()

    MONK_MULTISIG_CONTRACT = "cx0c436b120f3eabeb538b14fd30505917c3f35ee0"

    TICKER_TO_CONTRACT = {"OMM": "cx1a29259a59f463a67bb2ef84398b30ca56b5830a"}

    CONTRACT_TO_EXA = {
        "cx1a29259a59f463a67bb2ef84398b30ca56b5830a": 18,  # OMM
    }

    def __init__(self) -> None:
        pass

    def call(self, to: str, method: str, params: dict = {}):
        call = CallBuilder().to(to).method(method).params(params).build()
        try:
            result = self.ICON_SERVICE.call(call)
            return result
        except JSONRPCException as e:
            typer.echo(e)
            raise typer.Exit()

    def call_tx(self, to_address: str, method: str, params: dict = {}):
        transaction = (
            CallTransactionBuilder()
            .from_(self.WALLET_ADDRESS)
            .to(to_address)
            .nid(1)
            .value(0)
            .method(method)
            .params(params)
            .build()
        )
        try:
            signed_transaction = SignedTransaction(transaction, self.WALLET, 200000000)
            tx_hash = self.ICON_SERVICE.send_transaction(signed_transaction)
            return tx_hash
        except JSONRPCException as e:
            typer.echo(e)
            raise typer.Exit()
