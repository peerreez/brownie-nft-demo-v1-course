from brownie import AdvancedCollectible
from scripts.helpful_scripts import get_account, fund_with_link
from web3 import Web3

def main():
    account = get_account()
    advanced_collectible = AdvancedCollectible[-1]
    fund_with_link(advanced_collectible.address, amount = Web3.toWei(0.1, "ether"))
    creating_txn = advanced_collectible.createCollectible({"from": account})
    creating_txn.wait(1)
    print("New Puppies has been created")
