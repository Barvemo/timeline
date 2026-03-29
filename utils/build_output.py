import os
from datetime import datetime

def build_output(input_path, output_arg=None):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S_%f')

    base_path = output_arg or input_path
    output_folder = os.path.join(base_path, f"timeline_{timestamp}")

    os.makedirs(output_folder, exist_ok=True)

    output_file = os.path.join(output_folder, "timeline.xlsx")
    return output_file