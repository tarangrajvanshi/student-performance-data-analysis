import pandas as pd
import numpy as np

def load_data(path: str) -> pd.DataFrame:
    """Load the Mathematics student-performance CSV."""
    return pd.read_csv(path, sep=";")

def validate_data(df: pd.DataFrame) -> None:
    """Run basic data-quality checks."""
    print("Shape:", df.shape)
    print("\nMissing values:")
    print(df.isna().sum())
    print("\nDuplicate rows:", df.duplicated().sum())
    print("\nData types:")
    print(df.dtypes)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Apply conservative, reproducible cleaning steps."""
    result = df.copy()

    # Standardize categorical text.
    for col in result.select_dtypes(include="object").columns:
        result[col] = result[col].astype(str).str.strip().str.lower()

    # Remove exact duplicates only.
    result = result.drop_duplicates().reset_index(drop=True)

    # Validate final grade range rather than deleting unusual observations.
    invalid_g3 = result[(result["G3"] < 0) | (result["G3"] > 20)]
    print("Invalid G3 rows:", len(invalid_g3))

    return result

if __name__ == "__main__":
    # Example:
    # df = load_data("data/raw/student-mat.csv")
    # validate_data(df)
    # clean_df = clean_data(df)
    pass
