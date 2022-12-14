from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000
LOCAL_BLOCKCHAIN_ENVIROMENTS = ["development", "ganache-local"]
FORKED_LOCAL_ENVIROMENT = ["mainet-fork", "mainet-fork-dev"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS
        or network.show_active() in FORKED_LOCAL_ENVIROMENT
    ):
        return accounts[0]
    else:
        return accounts.load("GoerliAccount-1")


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print("Mocks Deployed")
