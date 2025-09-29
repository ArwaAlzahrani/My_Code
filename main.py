import pandas as pd
import matplotlib.pyplot as plt
import os

# Path to the dataset
data_path = "data/Full_dataset_blockchair_bitcoin_transactions_20250710.xls"

# Read Excel file
try:
    df = pd.read_excel(data_path)

    print("✅ Dataset loaded successfully.")
    print("📊 Showing first 5 rows:")
    print(df.head())

    # Check if 'size' or equivalent column exists
    if 'size' in df.columns:
        avg_size = df['size'].mean()
        print(f"\n📏 Average transaction size: {avg_size:.2f} bytes")

        # Plot histogram
        plt.figure(figsize=(8, 5))
        plt.hist(df['size'], bins=40, color='skyblue')
        plt.title("Distribution of Transaction Sizes")
        plt.xlabel("Size (bytes)")
        plt.ylabel("Frequency")
        plt.grid(True)

        # Save the plot
        os.makedirs("plots", exist_ok=True)
        plt.savefig("plots/transaction_sizes.png")
        print("📁 Plot saved in 'plots/transaction_sizes.png'")

    else:
        print("❌ 'size' column not found in the dataset.")

except Exception as e:
    print(f"❌ Error loading file: {e}")
