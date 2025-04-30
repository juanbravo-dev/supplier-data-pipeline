
import pandas as pd
from pathlib import Path
import logging
import sys

INPUT_DIR = Path("output")
OUTPUT_DIR = Path("cleaned")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = "transform.log"

logging.basicConfig(
    level= logging.INFO,
    format= "%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_FILE)
    ]
)

def clean_data (df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean a DataFrame:
    - Strip whitespace from column names
    - Lowercase and replace spaces with underscores
    - Strip whitespace from string cells
    - Fill missing values with empty strings
    """
    df.columns =  [col.strip().lower().replace(" ", "_") for col in df.columns]
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    df.fillna("", inplace=True)
    return df



if __name__ == "__main__":
    month = "january"  # hardcoded for now

    logging.info(f"Starting transformation for: {month}")

    input_file = INPUT_DIR / f"raw_extracted_{month}.csv"
    output_file = OUTPUT_DIR / f"cleaned_transformed_{month}.csv"

    df_raw = pd.read_csv(input_file)
    logging.info(f"Loaded file: {input_file.name} with shape {df_raw.shape}")

    df_clean = clean_data(df_raw)
    logging.info("Data cleaned successfully.")

    df_clean.to_csv(output_file, index=False)
    logging.info(f"Saved cleaned file to: {output_file}")
    
    print(f"✅ Cleaned file saved to: {output_file}")