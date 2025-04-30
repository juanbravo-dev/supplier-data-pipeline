
import pandas as pd
from pathlib import Path

INPUT_DIR = Path("output")
OUTPUT_DIR = Path("cleaned")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


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

    input_file = INPUT_DIR / f"raw_extracted_{month}.csv"
    output_file = OUTPUT_DIR / f"cleaned_transformed_{month}.csv"

    df_raw = pd.read_csv(input_file)
    df_clean = clean_data(df_raw)
    df_clean.to_csv(output_file, index=False)

    print(f"✅ Cleaned file saved to: {output_file}")