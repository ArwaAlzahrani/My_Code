import os
import pandas as pd
import matplotlib.pyplot as plt

# === SETUP: Define paths ===
data_dir = "My_Code/data"
plots_dir = "My_Code/plots"
input_filename = "Full_dataset_blockchair_bitcoin_transactions_20250710.xls"
summary_filename = "PQC_Blockchain_Impact_Summary.xlsx"

# === Ensure folders exist ===
os.makedirs(data_dir, exist_ok=True)
os.makedirs(plots_dir, exist_ok=True)

# === Load transaction data ===
# If you're using real data, make sure the file exists in the data directory
input_path = os.path.join(data_dir, input_filename)

if os.path.exists(input_path):
    # Load real Bitcoin transaction data from uploaded Excel file
    df_raw = pd.read_excel(input_path)
    
    # Assume the real file includes 'Signature Scheme' and 'Avg TX Size' columns
    df = df_raw[["Signature Scheme", "Avg TX Size", "Signature Size (bytes)", "Verification Time (ms)"]]
    df["Transactions per 1MB Block"] = (1_000_000 / df["Avg TX Size"]).astype(int)
else:
    # Fallback: use built-in sample data if real dataset not found
    print("Real dataset not found, using sample data...")
    sample_data = {
        "Signature Scheme": ["ECDSA", "Dilithium", "Falcon"],
        "Avg TX Size": [529, 5979, 1911],
        "Signature Size (bytes)": [70, 2420, 666],
        "Verification Time (ms)": [0.3, 0.5, 2.3]
    }
    df = pd.DataFrame(sample_data)
    df["Transactions per 1MB Block"] = (1_000_000 / df["Avg TX Size"]).astype(int)

# === Save Summary Table ===
summary_path = os.path.join(data_dir, summary_filename)
df.to_excel(summary_path, index=False)
print(f"\n📄 Summary Excel saved to: {summary_path}")

# === CHART 1: Average Transaction Size ===
plt.figure(figsize=(8, 5))
plt.bar(df["Signature Scheme"], df["Avg TX Size"], color='steelblue')
plt.title("Average Transaction Size per Signature Scheme")
plt.ylabel("Size (Bytes)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
chart_path1 = os.path.join(plots_dir, "avg_tx_size.png")
plt.savefig(chart_path1)
plt.close()

# === CHART 2: Throughput (Transactions per Block) ===
plt.figure(figsize=(8, 5))
plt.bar(df["Signature Scheme"], df["Transactions per 1MB Block"], color='seagreen')
plt.title("Approx. Transactions per 1MB Block")
plt.ylabel("Transactions")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
chart_path2 = os.path.join(plots_dir, "tx_per_block.png")
plt.savefig(chart_path2)
plt.close()

# === CHART 3: Verification Time ===
plt.figure(figsize=(8, 5))
plt.bar(df["Signature Scheme"], df["Verification Time (ms)"], color='coral')
plt.title("Signature Verification Time")
plt.ylabel("Time (ms)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
chart_path3 = os.path.join(plots_dir, "verification_time.png")
plt.savefig(chart_path3)
plt.close()

# === Final Message ===
print(f"Charts saved to: {plots_dir}")
print("\n PQC Blockchain Simulation Completed Successfully.")
