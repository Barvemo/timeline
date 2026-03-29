import os
from datetime import datetime

def build_output(input_path, output_arg=None):
    if output_arg:
        output_folder = os.path.join(output_arg, f"timeline_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S_%f')}")
    else:
        output_folder = os.path.join(input_path, f"timeline_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S_%f')}")

    os.makedirs(output_folder, exist_ok=True)

    output_file = os.path.join(output_folder, "timeline.xlsx")
    return output_file