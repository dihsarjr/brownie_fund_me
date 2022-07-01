from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import get_accounts


def deploy_fund_me():
    account = get_accounts()
    if network.show_active() != "development":
        price_field = config["networks"][network.show_active()]["eth_usd_price_field"]
    else:
        print(f"The network is {network.show_active()}")
        print("deploying fund me on the development network")
        moke_aggregator = MockV3Aggregator.deploy(
            18, 2000000000000000000000, {"from": account}
        )
        price_field = moke_aggregator.address
    fund_me = FundMe.deploy(
        price_field,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"FundMe contract address: {fund_me.address}")


def main():
    deploy_fund_me()
