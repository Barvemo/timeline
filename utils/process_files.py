import os, sys
import pandas as pd

def process_files(files, output_file):
    dfs = []
    skipped_files = []

    for f in files:
        f = Path(f)  # ensure Path object for each file, needed for absolute windows paths. in C: for example the : breaks path logic 

        if not f.is_file() or f.stat().st_size == 0:
            skipped_files.append(f)
            continue

        try:
            df = pd.read_csv(f, sep=None, engine="python", encoding="utf-8")
            dfs.append(df)
        except Exception as e:
            skipped_files.append(f)

    if not dfs:
        sys.exit(1)

    # Merge all
    merged = pd.concat(dfs, ignore_index=True)

    # Parse Timestamp column if present
    if "Timestamp" in merged.columns:
        merged["Timestamp"] = pd.to_datetime(merged["Timestamp"], errors="coerce")
        merged = merged.sort_values(by="Timestamp")

    # Export to Excel
    merged.to_excel(output_file, index=False)