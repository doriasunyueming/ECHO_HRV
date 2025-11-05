import pandas as pd

def load_raw_data():
    """
    TODO: Replace this with your real database pull.
    For now, just return an empty DataFrame or mock data.
    """
    return pd.DataFrame()

def save_clean_data(df: pd.DataFrame, path: str = "data/clean.csv"):
    """
    Save cleaned/processed data to the data/ folder.
    """
    df.to_csv(path, index=False)