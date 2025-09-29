# My_Code
This project was developed as part of an academic dissertation exploring real-world PQC readiness in blockchain systems, with the purpose of evaluating the impact of post-quantum signature schemes on blockchain scalability and performance.


-----------------------------------------------------------------


# Post-Quantum Signature Impact on Blockchain (Bitcoin Simulation)
This repository presents a simulation-based study on the real-world impact of integrating post-quantum cryptographic (PQC) digital signature schemes CRYSTALS-Dilithium and Falcon within Bitcoin transactions.
Built using Python and real transaction data (~65,000 transactions), the analysis models how these PQC algorithms affect:

-Transaction size 

-Throughput (transactions per block)

-Verification delays


-----------------------------------------------------------------

# Project Features

Empirical simulation using real Bitcoin data from Blockchair
Signature size inflation calculated per input, as per Bitcoin’s native signature model
Performance benchmarks estimated using PQClean
data for Dilithium and Falcon
Output graphs and stats for:

-Average transaction size

-Transactions per block (1MB limit)

-Comparative performance



-----------------------------------------------------------------
# Repository Structure

├── data/
│ └── bitcoin_transactions.csv # Cleaned transaction dataset

├── main.py # Core simulation and analysis script

├── plots/ # Generated graphs

├── README.md # Project description

└── requirements.txt # Required Python libraries**



-----------------------------------------------------------------

# Requirements
Install dependencies via:

pip install -r requirements.txt


Dependencies:

pandas

matplotlib

numpy

-----------------------------------------------------------------


# Run the Simulation
python main.py

-----------------------------------------------------------------


# Outputs:
Summary of PQC impact on Bitcoin block capacity

Signature inflation statistics

Verification timing insights

Comparison graphs

-----------------------------------------------------------------

# References

PQClean C Implementations

NIST Post-Quantum Cryptography Project

Blockchair Bitcoin API

