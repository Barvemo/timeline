#!/usr/bin/env python3

import argparse, os, sys, glob
from datetime import datetime
import pandas as pd

from utils.build_output import build_output
from utils.get_csv_files import get_csv_files
from utils.process_files import process_files
from utils.improve_excel import improve_excel

'''
TODO: Add logger, log file should be located in output folder with the resulting timeline.xlxs
TODO: split file into a main file, utils-file etc.
TODO: add readme
'''

def parse_args():
    parser = argparse.ArgumentParser(description="Merge CSV logs into an Excel timeline")
    parser.add_argument("-i", "--input", required=True, help="Input folder with CSV files")
    parser.add_argument("-o", "--output", required=False, help="Output folder for end product")
    return parser.parse_args()
    
def main():
    args = parse_args()
    input_path = os.path.abspath(args.input)

    files = get_csv_files(input_path)
    output_file = build_output(input_path, args.output)

    output_file, skipped = process_files(files, output_file)

    improve_excel(output_file)

if __name__ == "__main__":
    main()