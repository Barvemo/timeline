from pathlib import Path
from datetime import datetime

def build_output(input_path, output_arg=None):
    # Ensure Path objects
    input_path = Path(input_path)
    base_path = Path(output_arg) if output_arg else input_path

    # If base_path is absolute, separate the drive from the rest
    if base_path.drive:
        # base_path.drive contains 'C:'
        drive = Path(base_path.drive + "\\")  # keeps the drive
        rest = base_path.relative_to(base_path.anchor)  # 'Users/name/...'
        base_path = drive / rest  # safely construct the absolute path
    # else do nothing for relative paths

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S_%f')
    output_folder = base_path / f"timeline_{timestamp}"
    output_folder.mkdir(parents=True, exist_ok=True)

    output_file = output_folder / "timeline.xlsx"
    return output_file