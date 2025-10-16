import pandas as pd
import os

def load_disease_data():
    """Load the disease precautions CSV file."""
    csv_path = os.path.join(os.path.dirname(__file__), 'data', 'Disease_precaution.csv')
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found at {csv_path}")
    
    df = pd.read_csv(csv_path)
    # Handle empty columns by filling NaN with empty string
    df = df.fillna('')
    # Strip whitespace from disease names to handle trailing spaces (e.g., "Diabetes ")
    df['Disease'] = df['Disease'].str.strip()
    return df

def find_precautions(disease_name):
    """Find precautions for a given disease name."""
    df = load_disease_data()
    
    # Find exact match (case-insensitive)
    matching_row = df[df['Disease'].str.lower() == disease_name.lower()]
    
    if matching_row.empty:
        return None
    
    row = matching_row.iloc[0]
    precautions = [
        row['Precaution_1'],
        row['Precaution_2'],
        row['Precaution_3'],
        row['Precaution_4']
    ]
    # Filter out empty strings
    precautions = [p.strip() for p in precautions if p.strip()]
    
    return ', '.join(precautions)