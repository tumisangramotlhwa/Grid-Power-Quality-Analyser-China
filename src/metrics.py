from pathlib import Path
import pandas as pd

if __name__ == "__main__":
    file_path = Path('data') / 'panel_aggregate.csv'
    if file_path.exists():
        df = pd.read_csv(file_path)
        print("DataFrame loaded successfully!")
    else:
        print("File not found. Make sure loader.py has run first.")

def compute_rolling_stats(df, column, windows=("5min", "10min", "30min"),):
    df = df.copy()
    for w in windows:
        df[f"{column}_mean_{w}"] = df[column].rolling(w).mean()
        df[f"{column}_max_{w}"] = df[column].rolling(w).max()
        df[f"{column}_std_{w}"] = df[column].rolling(w).std()
    return df

# Convenience wrapper

def add_rolling_metrics( df, columns, windows=("5min", "10min", "30min")):
    df = df.copy()
    for col in columns:
        df = compute_rolling_stats(df, col, windows)

    return df