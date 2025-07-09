import csv
import os

# Path to the CSV file (relative to this script)
CSV_PATH = os.path.join(os.path.dirname(__file__), 'inputs.csv')

def load_test_data(csv_path=CSV_PATH):
    """
    Reads the CSV file and returns a list of dictionaries.
    Each dictionary represents a row with keys as column headers.
    """
    data = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data 