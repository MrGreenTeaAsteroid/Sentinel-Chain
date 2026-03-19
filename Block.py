import hashlib
import json

class Block:
    def __init__(self,previous_hash,transaction_data,risk_score):
        self.transaction = transaction_data
        self.risk_score = risk_score
        self.previous_hash = previous_hash

        # We combine the TX data, the link to the past (prev_hash),
        # and the ML verdict (risk_score) into one unique fingerprin
        tx_string = json.dumps(transaction_data, sort_keys=True)
        string_to_hash = tx_string + str(previous_hash)+str(risk_score)

        self.block_hash = hashlib.sha256(string_to_hash.encode()).hexdigest()