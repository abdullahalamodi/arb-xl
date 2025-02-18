import json
import pandas as pd
from pathlib import Path

def read_json(file_path):
    """Reads a JSON file and returns its data as a dictionary."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
    
def write_json(file_path, data):
    """Writes a dictionary to a JSON file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def read_xls(file_path):
    """Reads an Excel file and returns a DataFrame."""
    return pd.read_excel(file_path, engine='openpyxl')

def write_xls(file_path, data_frame):
    """Writes a DataFrame to an Excel file."""
    data_frame.to_excel(file_path, index=False, engine='openpyxl')
