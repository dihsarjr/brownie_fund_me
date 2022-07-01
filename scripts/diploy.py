from brownie import FundMe, network, config
from scripts.helpful_scripts import get_accounts




def deploy_fund_me():
    account = get_accounts()
    if network.show_active() == "development":
        price_field = config["networks"][network.show_active()]["price_field"]
     
    fund_me = FundMe.deploy(price_field,{"from": account}, publish_source=True)
    print(f"FundMe contract address: {fund_me.address}")


def main():
    deploy_fund_me()
