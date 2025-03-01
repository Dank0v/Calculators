import tkinter as tk
import subprocess

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dankov's Calculators")
        self.root.geometry("400x300")

        tk.Label(root, text="Main Window", font=("Arial", 14)).pack(pady=10)

        # Create buttons to open different windows
        self.create_button("Parallel Resistance Sigma", "parallel_sigma.py")
        self.create_button("Series Resistance Sigma", "series_sigma.py")
        self.create_button("Open Window 3", "window3.py")

    def create_button(self, text, script_name):
        """Creates a button that opens a new window."""
        button = tk.Button(self.root, text=text, font=("Arial", 12),
        command=lambda: self.open_new_window(script_name))
        button.pack(pady=5)

    def open_new_window(self, script_name):
        """Opens a new window using a separate script."""
        subprocess.Popen(["python", script_name])

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
