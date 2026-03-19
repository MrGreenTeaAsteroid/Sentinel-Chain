from Block import Block
from sentinel_chain import Sentinel_chain
import json

def run_demo():
    sc = Sentinel_chain()

    print("--Initializing regular transaction--")
    sc.process_transaction({
#defining a regular test transaction

        'amount_usd':5000,
        'gas_fee_usd':20,
        'tx_velocity_sec':3600,
        'address_age_days': 500,
        'hour_of_day':14,
        'is_whitelisted':1
    })
#defining a potential anomaly
    print("--Initializing potentially unusual transaction--")
    sc.process_transaction({
        'amount_usd': 85000,
        'gas_fee_usd': 400,
        'tx_velocity_sec': 10,
        'address_age_days': 1,
        'hour_of_day': 3,
        'is_whitelisted': 0
    })


#Integrity check
    valid, msg= sc.validate_integrity()
    print(f"\nSecurity Audit Result: {msg}")

if __name__ == "__main__":
    run_demo()