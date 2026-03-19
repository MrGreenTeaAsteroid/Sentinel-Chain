# 🛡️ Sentinel-Chain: ML-Augmented Blockchain Ledger

A security-first blockchain implementation that utilizes **Unsupervised Machine Learning** to vet transactions before they are committed to the immutable ledger.

### 🧠 Core Technology
* **Anomaly Detection:** Powered by an **Isolation Forest** model to identify high-risk transaction patterns (Amount vs. Time vs. Wallet Age).
* **Cryptographic Integrity:** SHA-256 hashing ensures that the ledger and the associated ML risk scores remain tamper-proof.
* **Real-Time Dashboard:** Built with **Streamlit** for live monitoring and interactive "stress-testing" of the security engine.

### 🛠️ Technical Stack
* **Language:** Python 3.11+
* **ML Library:** Scikit-Learn (Isolation Forest)
* **Web UI:** Streamlit
* **Environment:** Fedora Linux / PyCharm
