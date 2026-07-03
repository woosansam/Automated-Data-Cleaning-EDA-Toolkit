import pandas as pd
import sys

def main(file_path):
    print(f"Loading data from {file_path}...")
    df = pd.read_csv(file_path)
    print("Data successfully loaded!")
    print(df.head())
    print(df.describe())

if __name__ == "__main__":
    main('data/sample_data.csv')
