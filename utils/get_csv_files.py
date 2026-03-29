from pathlib import Path
import sys

def get_csv_files(input_path):
    input_path = Path(input_path)  # ensure Path object
    files = sorted(input_path.glob("*.csv"))  # Path.glob works cross-platform

    if not files:
        sys.exit("No CSV files found in the input folder.")

    return files