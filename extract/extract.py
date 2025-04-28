"""
Extraction of first montly CSV report.

"""
import logging
import pandas as pd
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DATA_DIR = Path("data")
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def read_csv(input_path: Path) -> pd.DataFrame:
    logging.info(f"Reading file: {input_path}")
    df = pd.read_csv(input_path, encoding='latin1', delimiter=';', decimal=',')
    logging.info(f"File {input_path.name} read successfully with shape {df.shape}")
    return df

def save_csv(df: pd.DataFrame, output_path: Path):
    logging.info(f"Saving extracted data to: {output_path}")
    df.to_csv(output_path, index=False)
    logging.info(f"💾 Data saved successfully to {output_path}")

def main():
    month_name = "january"

    input_filename = f"{month_name}_consumption_report.csv"
    output_filename = f"raw_extracted_{month_name}.csv"

    input_file = DATA_DIR / input_filename
    output_file = OUTPUT_DIR / output_filename

    df = read_csv(input_file)
    save_csv(df, output_file)
    logging.info(f"✅ Extraction finished for {month_name.upper()}")

if __name__ == "__main__":
    
    main()

