"""
Extraction of first montly CSV report.

"""

import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def read_csv(input_path: Path) -> pd.DataFrame:
    df = pd.read_csv(input_path, encoding='latin1', delimiter=';', decimal=',')
    return df

def save_csv(df: pd.DataFrame, output_path: Path):
    df.to_csv(output_path, index=False)

def main():
    month_name = "january"

    input_filename = f"{month_name}_consumption_report.csv"
    output_filename = f"raw_extracted_{month_name}.csv"

    input_file = DATA_DIR / input_filename
    output_file = OUTPUT_DIR / output_filename

    df = read_csv(input_file)
    save_csv(df, output_file)

if __name__ == "__main__":
    main()

