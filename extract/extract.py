"""
Extraction of first monthly CSV report.

"""
import sys
import argparse
import logging
import pandas as pd
from pathlib import Path

LOG_FILE = "extractor.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_FILE)
    ]
)

DATA_DIR = Path("data")
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

VALID_MONTHS = {
    "january", "february", "march", "april", "may", "june",
    "july", "august", "september", "october", "november", "december"
}

def validate_month(month: str) -> str:
    month = month.lower()
    if month not in VALID_MONTHS:
        logging.error(f"❌ Invalid month name: '{month}'. Valid options: {sorted(VALID_MONTHS)}")
        sys.exit(1)
    return month

def read_csv(input_path: Path) -> pd.DataFrame:
    logging.info(f"Reading file: {input_path}")
    df = pd.read_csv(input_path, encoding='latin1', delimiter=';', decimal=',')
    logging.info(f"File {input_path.name} read successfully with shape {df.shape}")
    return df

def save_csv(df: pd.DataFrame, output_path: Path):
    logging.info(f"Saving extracted data to: {output_path}")
    df.to_csv(output_path, index=False)
    logging.info(f"💾 Data saved successfully to {output_path}")

def main(month_name: str):

    month_name = validate_month(month_name)

    input_filename = f"{month_name}_consumption_report.csv"
    output_filename = f"raw_extracted_{month_name}.csv"

    input_file = DATA_DIR / input_filename
    output_file = OUTPUT_DIR / output_filename

    df = read_csv(input_file)
    save_csv(df, output_file)
    logging.info(f"✅ Extraction finished for {month_name.upper()}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract monthly supplier consumption report.")
    parser.add_argument(
        "month",
        type=str,
        help="Month name to process (e.g., 'january', 'february', etc.)"
    )
    args = parser.parse_args()
    
    main(args.month)

