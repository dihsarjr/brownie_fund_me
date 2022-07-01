from brownie import FundMe
from scripts.helpful_scripts import get_accounts

def deploy_fund_me():
    account = get_accounts()
    fund_me = FundMe.deploy({'from': account})
    print(f"FundMe contract address: {fund_me.address}")

def main():
    deploy_fund_me() 
