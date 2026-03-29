#!/usr/bin/env python3

import argparse, os, sys, glob
from datetime import datetime

from utils.build_output import build_output
from utils.get_csv_files import get_csv_files
from utils.process_files import process_files
from utils.improve_excel import improve_excel
from logger.logger_config import logger_config

def parse_args():
    parser = argparse.ArgumentParser(description="Merge CSV logs into an Excel timeline")
    parser.add_argument("-i", "--input", required=True, help="Input folder with CSV files")
    parser.add_argument("-o", "--output", required=False, help="Output folder for end product")
    return parser.parse_args()
    
def main():
    args = parse_args()
    input_path = os.path.abspath(args.input)
    output_file = build_output(input_path, args.output)
    log_file = os.path.join(os.path.dirname(output_file), "timeline_script.log")
    logger = logger_config(log_file)

    files = get_csv_files(input_path)

    process_files(files, output_file)
    improve_excel(output_file)

if __name__ == "__main__":
    main()