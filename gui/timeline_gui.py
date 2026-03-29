import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

from utils.build_output import build_output
from utils.get_csv_files import get_csv_files
from utils.process_files import process_files
from utils.improve_excel import improve_excel


def run_gui():
    root = tk.Tk()
    root.title("Timeline Tool")
    root.geometry("500x250")

    # Path variables
    input_path = tk.StringVar()
    output_path = tk.StringVar()

    # Folder selection
    def browse_input():
        folder = filedialog.askdirectory(title="Select Input Folder")
        if folder:
            input_path.set(str(Path(folder).resolve()))

    def browse_output():
        folder = filedialog.askdirectory(title="Select Output Folder")
        if folder:
            output_path.set(str(Path(folder).resolve()))

    # Run timeline
    def run_script():
        if not input_path.get():
            messagebox.showerror("Error", "Please select an input folder")
            return

        try:
            input_folder = Path(input_path.get())
            output_folder = Path(output_path.get()) if output_path.get() else None

            files = get_csv_files(input_folder)
            if not files:
                messagebox.showerror("Error", f"No CSV files found in {input_folder}")
                return

            output_file = build_output(input_folder, output_folder)
            process_files(files, output_file)
            improve_excel(output_file)
            messagebox.showinfo("Success", f"Timeline created at:\n{output_file}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # GUI Layout
    tk.Label(root, text="Input Folder:").pack(pady=(10, 0))
    tk.Entry(root, textvariable=input_path, width=60).pack()
    tk.Button(root, text="Browse", command=browse_input).pack(pady=5)

    tk.Label(root, text="Output Folder:").pack(pady=(10, 0))
    tk.Entry(root, textvariable=output_path, width=60).pack()
    tk.Button(root, text="Browse", command=browse_output).pack(pady=5)

    tk.Button(root, text="Run", command=run_script, bg="green", fg="white").pack(pady=15)

    root.mainloop()