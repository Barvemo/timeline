import os, glob

def get_csv_files(input_path):
    files = sorted(glob.glob(os.path.join(input_path, "*.csv")))
    if not files:
        sys.exit(1)
    return files