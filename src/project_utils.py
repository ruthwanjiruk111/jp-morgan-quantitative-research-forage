import pandas as pd
import numpy as np



def load_data(file_path="Nat_Gas.csv"):
    """
    Load and prepare the natural gas price dataset.
    """
    df = pd.read_csv(file_path)
    df["Dates"] = pd.to_datetime(df["Dates"], format="%m/%d/%y")
    df.set_index("Dates", inplace=True)
    return df