#!/usr/bin/env python3

import argparse, os, sys, glob
from pathlib import Path
from datetime import datetime

from utils.build_output import build_output
from utils.get_csv_files import get_csv_files
from utils.process_files import process_files
from utils.improve_excel import improve_excel
from logger.logger_config import logger_config
from gui.timeline_gui import run_gui

def parse_args():
    parser = argparse.ArgumentParser(description="Merge CSV logs into an Excel timeline")
    parser.add_argument("-i", "--input", required=True, help="Input folder with CSV files")
    parser.add_argument("-o", "--output", required=False, help="Output folder for end product")
    return parser.parse_args()

def main():
    args = parse_args()

    # Convert input and optional output to Path objects
    input_path = Path(args.input)
    output_arg = Path(args.output) if args.output else None

    # Make absolute paths safely
    input_path = input_path.resolve()
    if output_arg:
        output_arg = output_arg.resolve()

    output_file = build_output(input_path, output_arg)

    log_file = output_file.parent / "timeline_script.log"
    logger = logger_config(log_file)

    files = get_csv_files(input_path)

    process_files(files, output_file)
    improve_excel(output_file)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main()
    else:
        run_gui()