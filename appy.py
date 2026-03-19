import streamlit as st
import pandas as pd
# FIX: Match the filename exactly (removed the extra 'i' in sentinel)
from sentinel_chain import Sentinel_chain

st.set_page_config(page_title="Sentinel-Chain:", layout="wide")
st.title("Sentinel-Chain: ML-Guard Ledger")


if 'sc' not in st.session_state:
    try:
        st.session_state.sc = Sentinel_chain()
    except FileNotFoundError:
        st.error("❌ ML Model not found! Run 'python generate_data.py' first.")
        st.stop()

with st.sidebar:
    st.header("Transaction Entry")
    amt = st.number_input("Amount (USD)", 0, 1000000, 75000)
    gas = st.number_input("Gas Fee (USD)", 0, 1000, 15)
    vel = st.number_input("Seconds Since Last Tx", 0, 86400, 7200)
    age = st.number_input("Wallet Age (Days)", 0, 2000, 500)
    hr = st.slider("Hour of Day", 0, 23, 14)
    white = st.checkbox("Whitelisted Address?", value=True)

    if st.button("Execute Transaction"):
        tx = {
            'amount_usd': float(amt),
            'gas_fee_usd': float(gas),
            'tx_velocity_sec': float(vel),
            'address_age_days': int(age),
            'hour_of_day': int(hr),
            'is_whitelisted': int(white)
        }

        # Call the process logic
        success = st.session_state.sc.process_transaction(tx)

        if success:
            st.success("Transaction Approved & Block Mined!")
        else:
            st.error("Transaction Rejected by ML Sentinel!")


st.subheader("Immutable Audit Log")
for i, block in enumerate(reversed(st.session_state.sc.chain)):

    real_idx = len(st.session_state.sc.chain) - 1 - i
    with st.expander(f"Block {real_idx} | Hash: {block.block_hash[:12]}..."):
        st.json(block.transaction)

        st.metric("ML Risk Score", f"{block.risk_score:.4f}")