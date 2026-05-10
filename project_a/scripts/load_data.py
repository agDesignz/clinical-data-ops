import pandas as pd
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

def load_data(file):
    path = os.path.join(DATA_DIR, f"{file}.csv")
    return pd.read_csv(path)

