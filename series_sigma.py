import tkinter as tk
from tkinter import ttk
import math
import subprocess

def calculate_uncertainty(*args):
    try:
        # Get values from input fields
        R1 = float(r1_var.get())
        sigma1 = float(sigma1_var.get())
        R2 = float(r2_var.get())
        sigma2 = float(sigma2_var.get())
        
        # Check for division by zero
        if R1 <= 0 or R2 <= 0 or (R1 + R2) <= 0:
            r_eq_var.set("N/A")
            sigma_r_eq_var.set("N/A")
            return

        # Calculate equivalent resistance
        R_eq = R1 + R2
        
        # Calculate uncertainty of equivalent resistance
        sigma_R_eq = math.sqrt(sigma1**2 + sigma2**2)
        
        # Update result fields
        r_eq_var.set(f"{R_eq:.2f}")
        sigma_r_eq_var.set(f"{sigma_R_eq:.2f}")
        
    except ValueError:
        # Handle empty or invalid inputs
        r_eq_var.set("Invalid input")
        sigma_r_eq_var.set("Invalid input")

def open_python_script():
    try:
        # Specify the path to the Python script you want to run
        script_path = "main.py"  # Change this path to your Python script
        subprocess.Popen(["python", script_path])
    except Exception as e:
        print(f"Error running script: {e}")

# Create the main window
root = tk.Tk()
root.title("Series Resistance Calculator")
root.geometry("450x650")  # Start with a larger size
root.minsize(450, 650)    # Increased minimum size to ensure all elements are visible

# Create style
style = ttk.Style()
style.configure("TFrame", background="#f0f0f0")
style.configure("TLabel", background="#f0f0f0", font=("Arial", 10))
style.configure("TButton", font=("Arial", 10))
style.configure("TEntry", font=("Arial", 10))
style.configure("Header.TLabel", font=("Arial", 12, "bold"))
style.configure("Result.TLabel", background="#e0e0e0", font=("Arial", 10, "bold"))

# Main frame with padding
main_frame = ttk.Frame(root, padding="20", style="TFrame")
main_frame.pack(fill="both", expand=True)

# Configure rows and columns to make them scalable
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
for i in range(8):
    main_frame.rowconfigure(i, weight=1)

# Title
title_label = ttk.Label(main_frame, text="Series Resistance Calculator", style="Header.TLabel")
title_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")

# Variables for input fields (default to 0)
r1_var = tk.StringVar(value="0")
sigma1_var = tk.StringVar(value="0")
r2_var = tk.StringVar(value="0")
sigma2_var = tk.StringVar(value="0")
r_eq_var = tk.StringVar(value="N/A")
sigma_r_eq_var = tk.StringVar(value="N/A")

# Input section frame
input_frame = ttk.LabelFrame(main_frame, text="Input Values", padding="10")
input_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)
input_frame.columnconfigure(0, weight=1)
input_frame.columnconfigure(1, weight=1)

# Create input fields with more padding and larger entry width
ttk.Label(input_frame, text="R1 [Ω]:").grid(row=0, column=0, sticky="w", padx=10, pady=8)
r1_entry = ttk.Entry(input_frame, textvariable=r1_var, width=20)
r1_entry.grid(row=0, column=1, sticky="ew", padx=10, pady=8)

ttk.Label(input_frame, text="σ(R1) [Ω] - Std. Dev. of R1:").grid(row=1, column=0, sticky="w", padx=10, pady=8)
sigma1_entry = ttk.Entry(input_frame, textvariable=sigma1_var, width=20)
sigma1_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=8)

ttk.Label(input_frame, text="R2 [Ω]:").grid(row=2, column=0, sticky="w", padx=10, pady=8)
r2_entry = ttk.Entry(input_frame, textvariable=r2_var, width=20)
r2_entry.grid(row=2, column=1, sticky="ew", padx=10, pady=8)

ttk.Label(input_frame, text="σ(R2) [Ω] - Std. Dev. of R2:").grid(row=3, column=0, sticky="w", padx=10, pady=8)
sigma2_entry = ttk.Entry(input_frame, textvariable=sigma2_var, width=20)
sigma2_entry.grid(row=3, column=1, sticky="ew", padx=10, pady=8)

# Results section in a frame
result_frame = ttk.LabelFrame(main_frame, text="Results", padding="10")
result_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)
result_frame.columnconfigure(0, weight=1)
result_frame.columnconfigure(1, weight=1)

# Results with better spacing and prominence
ttk.Label(result_frame, text="Req [Ω] - Equivalent Resistance:").grid(row=0, column=0, sticky="w", padx=10, pady=8)
ttk.Label(result_frame, textvariable=r_eq_var, style="Result.TLabel", width=20).grid(row=0, column=1, sticky="ew", padx=10, pady=8)

ttk.Label(result_frame, text="σ(Req) [Ω] - Std. Dev. of Req:").grid(row=1, column=0, sticky="w", padx=10, pady=8)
ttk.Label(result_frame, textvariable=sigma_r_eq_var, style="Result.TLabel", width=20).grid(row=1, column=1, sticky="ew", padx=10, pady=8)

# Formulas section in a frame
formula_frame = ttk.LabelFrame(main_frame, text="Formulas Used", padding="10")
formula_frame.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)
formula_frame.columnconfigure(0, weight=1)

# Formula text with clear formatting and spacing
formulas_text = """
Req = R1 + R2

σ(Req) = √(σ(R1)² + σ(R2)²)
"""

formula_label = ttk.Label(formula_frame, text=formulas_text, background="#e8e8e8", padding=10)
formula_label.grid(row=0, column=0, sticky="ew", padx=10, pady=8)

# Set up event bindings for real-time calculation
r1_var.trace_add("write", calculate_uncertainty)
sigma1_var.trace_add("write", calculate_uncertainty)
r2_var.trace_add("write", calculate_uncertainty)
sigma2_var.trace_add("write", calculate_uncertainty)

# Calculate initial values
calculate_uncertainty()

# Add a button to run the Python script
open_button = ttk.Button(main_frame, text="Return to Main Window", command=open_python_script)
open_button.grid(row=4, column=0, columnspan=2, pady=10)

# Start the event loop
if __name__ == "__main__":
    root.mainloop()