# omm-monk-cli

This is a tool that Omm monks can use to manage the Monks' multisignature wallet.

## Installation

omm-monk-cli is a Python package. To use it, you'll need to install a few dependencies.

* For managing Python environments and versions, I recommend installing [pyenv](https://github.com/pyenv/pyenv).
* For installing and managing package dependnecies, I recommend installing [Poetry](https://python-poetry.org).

### Install Python 3.10.2

```
pyenv install 3.10.2
```

### Clone Repo

```
git clone https://github.com/bwhli/omm-monk-cli.git
```

### Install Dependecies

```
cd omm-monk-cli
poetry shell
poetry install
```

## Commands

### Submit Token Transfer

```
monk submit-token-transfer VALUE TOKEN_CONTRACT TO_ADDRESS
```

* `VALUE`: The amount of tokens you want to transfer (e.g. 1 OMM = 1, 10 bnUSD = 10).
* `TOKEN_CONTRACT`: The contract address of the token you want to transfer.
* `TO_ADDRESS`: The destination address you want to transfer tokens to.

### Confirm Transaction

```
monk confirm-transaction TRANSACTION_ID
```

* `TRANSACTION_ID`: The ID number of the transaction you want to confirm.