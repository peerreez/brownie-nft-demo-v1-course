from brownie import network, AdvancedCollectible
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS, fund_with_link
import time
import pytest

def test_can_create_advanced_collectible_integration():
    # deploy the contract
    # create an NFT
    # get a random breed back
    # Arrange
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("This test is only for integrations environments")
    # Act
    advanced_collectible = AdvancedCollectible[-1]
    fund_with_link(advanced_collectible.address)
    creating_tx = advanced_collectible.createCollectible({"from": get_account(), "gas": 500000})  # Adjust as needed
    creating_tx.wait(1)
    time.sleep(60)
    # Assert
    print(advanced_collectible.tokenCounter())
    assert advanced_collectible.tokenCounter() > 1

