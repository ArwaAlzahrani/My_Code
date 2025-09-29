import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Load the dataset
DATA_PATH = "data/Full_dataset_blockchair_bitcoin_transactions_20250710.xls"
df = pd.read_excel(DATA_PATH)

# Constants
ECDSA_SIG_SIZE = 70  # Approximate size per signature (bytes)
DILITHIUM_SIG_SIZE = 2420  # Approximate Dilithium-III signature size
FALCON_SIG_SIZE = 900  # Approximate Falcon-512 signature size
BLOCK_SIZE_LIMIT = 1_000_000  # 1 MB in bytes

# Calculate signature inflation
df["ecdsa_total_sig_size"] = df["input_count"] * ECDSA_SIG_SIZE
df["dilithium_total_sig_size"] = df["input_count"] * DILITHIUM_SIG_SIZE
df["falcon_total_sig_size"] = df["input_count"] * FALCON_SIG_SIZE

# Recalculate transaction sizes
df["tx_size_ecdsa"] = df["tx_size"] - df["ecdsa_total_sig_size"] + df["ecdsa_total_sig_size"]
df["tx_size_dilithium"] = df["tx_size"] - df["ecdsa_total_sig_size"] + df["dilithium_total_sig_size"]
df["tx_size_falcon"] = df["tx_size"] - df["ecdsa_total_sig_size"] + df["falcon_total_sig_size"]

# Average size calculations
avg_tx_size_ecdsa = df["tx_size_ecdsa"].mean()
avg_tx_size_dilithium = df["tx_size_dilithium"].mean()
avg_tx_size_falcon = df["tx_size_falcon"].mean()

# Transactions per block
txs_per_block_ecdsa = BLOCK_SIZE_LIMIT // avg_tx_size_ecdsa
txs_per_block_dilithium = BLOCK_SIZE_LIMIT // avg_tx_size_dilithium
txs_per_block_falcon = BLOCK_SIZE_LIMIT // avg_tx_size_falcon

# Print results
print("=== Average Transaction Sizes ===")
print(f"ECDSA:     {avg_tx_size_ecdsa:.2f} bytes")
print(f"Dilithium: {avg_tx_size_dilithium:.2f} bytes")
print(f"Falcon:    {avg_tx_size_falcon:.2f} bytes\n")

print("=== Estimated Transactions per 1MB Block ===")
print(f"ECDSA:     {txs_per_block_ecdsa:.0f} tx")
print(f"Dilithium: {txs_per_block_dilithium:.0f} tx")
print(f"Falcon:    {txs_per_block_falcon:.0f} tx\n")

# Plotting
if not os.path.exists("plots"):
    os.makedirs("plots")

# Bar chart for average size
plt.figure(figsize=(8, 5))
plt.bar(["ECDSA", "Dilithium", "Falcon"],
        [avg_tx_size_ecdsa, avg_tx_size_dilithium, avg_tx_size_falcon],
        color=["green", "blue", "orange"])
plt.title("Average Transaction Size by Signature Scheme")
plt.ylabel("Size (bytes)")
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.savefig("plots/average_transaction_size.png")
plt.close()

# Bar chart for tx/block
plt.figure(figsize=(8, 5))
plt.bar(["ECDSA", "Dilithium", "Falcon"],
        [txs_per_block_ecdsa, txs_per_block_dilithium, txs_per_block_falcon],
        color=["green", "blue", "orange"])
plt.title("Estimated Transactions per Block (1MB)")
plt.ylabel("Transactions")
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.savefig("plots/transactions_per_block.png")
plt.close()
