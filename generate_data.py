import pandas as pd
import numpy as np
from joblib import dump
from sklearn.ensemble import IsolationForest

def generate_training_data(n_samples=5000):
    np.random.seed(42)
    # simulates normal activity
    data = {
        'amount_usd': np.random.normal(75000, 20000, n_samples),
        'gas_fee_usd': np.random.normal(15, 5, n_samples),
        'tx_velocity_sec': np.random.exponential(7200, n_samples),
        'address_age_days': np.random.randint(90, 1500, n_samples),
        'hour_of_day': np.random.choice(np.arange(9, 18), n_samples),  # 9-5 hours
        'is_whitelisted': np.random.choice([1, 0], n_samples, p=[0.95, 0.05])
    }

    df = pd.DataFrame(data).clip(lower=0)

    # Trains Isolation Forest (1% anomaly rate)
    model = IsolationForest(contamination=0.01, random_state=42)
    model.fit(df)

    dump(model, 'sentinel_model.joblib')
    df.to_csv('normal_history.csv', index=False)
    print("✅ Model trained: 'sentinel_model.joblib' created.")

# FIX: This block MUST be moved to the far left margin (un-indented)
if __name__ == "__main__":
    generate_training_data()