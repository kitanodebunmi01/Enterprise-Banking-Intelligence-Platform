import pandas as pd

file = r"C:\Users\user\Documents\Documents\Projects\Enterprise Banking Intelligence & Early Warning Platform (EBIEWP)\Data\Facts\FactTransaction.csv"

print("Counting rows...")

rows = sum(1 for _ in open(file, encoding="utf-8")) - 1

print(f"Rows: {rows:,}")