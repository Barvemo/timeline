# Timeline Script

A script that merges data from multiple CSV files into a single Excel file with formatting.
Designed to run from a USB drive without requiring Python or internet access.

## Features

- Works without Python installed
- Runs from USB without installing Python/packages or having internet access.

## Requirements

- Windows 10+ for standalone executable `timeline.exe`
- Linux/macOS (no standalone executable at the moment)
- Optional: Python 3.11 for rebuilding or modifying the script

## Installation / Setup

1. Copy timeline.exe (windows only) or repository to USB/computer.
2. Run script; input argument required, output argument optional.

## Usage
### Command-line example

```bash
# print script usage help
timeline.exe --help

# using path relative to script
timeline.exe --input input_folder

# using an absolute path
timeline.exe --input E:\data\input_data

# using optional output folder argument
timeline.exe --input F:\MYUSB\parsed_kape_data --output F:\MYUSB\folder_i_want_the_output_in_thank_you
```

## Rebuilding / Development
### 1. Activate virtual environment
**Windows**
```
venv\Scripts\activate
```

**Linux/macOS**
```
source venv/bin/activate
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Build standalone executable (after making desired changes)
```
pyinstaller --onefile timeline.py
```