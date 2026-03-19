import pandas as pd
from joblib import load
from Block import Block


class Sentinel_chain:
    def __init__(self):

        self.chain = []
        self.features = ['amount_usd', 'gas_fee_usd', 'tx_velocity_sec',
                         'address_age_days', 'hour_of_day', 'is_whitelisted']
        try:
            self.model = load('sentinel_model.joblib')
        except:
            raise FileNotFoundError("Model not found. Please run generate_data.py first.")

        # Initialize Genesis
        self.add_to_chain({"info": "Genesis"}, 0.0, "0" * 64)

    def add_to_chain(self, data, risk, prev_hash):
        new_block = Block(prev_hash, data, risk)
        self.chain.append(new_block)
        return new_block

    def process_transaction(self, tx):

        df = pd.DataFrame([tx])[self.features]

        # Risk Analysis
        # 1 = Normal, -1 = Anomaly
        prediction = self.model.predict(df)[0]
        risk_score = self.model.decision_function(df)[0]

        if prediction == -1:
            print(f"REJECTED: Anomaly Detected (Score: {risk_score:.4f})")
            return False

        # Add to Ledger
        prev_h = self.chain[-1].block_hash
        self.add_to_chain(tx, risk_score, prev_h)
        print(f"APPROVED: Added to Block {len(self.chain) - 1}")
        return True

    def validate_integrity(self):
        for i in range(1, len(self.chain)):
            curr, prev = self.chain[i], self.chain[i - 1]
            if curr.previous_hash != prev.block_hash:  # FIX: Indented this correctly
                return False, f"Broken link at Block {i}"
        return True, "Chain Secure."