import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import hashlib
import pyperclip

def compute_hash():
    algorithm = hash_algorithm.get()
    data = entry_data.get()

    if algorithm == "Select" or not data:
        messagebox.showwarning("Incomplete Input", "Please select a hash algorithm and enter data.")
        return

    hash_func = hashlib.new(algorithm.lower())
    hash_func.update(data.encode('utf-8'))
    hashed_data = hash_func.hexdigest()

    label_hash_result.config(text=f"{algorithm} Hash: {hashed_data}")
    button_copy.config(state=tk.NORMAL)

def copy_to_clipboard():
    result = label_hash_result.cget("text").split(":")[-1].strip()
    pyperclip.copy(result)
    messagebox.showinfo("Copied to Clipboard", "Hash result copied to clipboard.")

# Create the main application window
app = tk.Tk()
app.title("Hash Function")

# Add elements
label_instruction = tk.Label(app, text="Enter your data:")
label_instruction.pack()

entry_data = tk.Entry(app)
entry_data.pack()

hash_algorithm = ttk.Combobox(app, values=["MD5", "SHA-1", "SHA-256", "SHA-512"])
hash_algorithm.set("Select")
hash_algorithm.pack()

button_compute = tk.Button(app, text="Compute Hash", command=compute_hash)
button_compute.pack()

button_copy = tk.Button(app, text="Copy to Clipboard", state=tk.DISABLED, command=copy_to_clipboard)
button_copy.pack()

label_hash_result = tk.Label(app, text="")
label_hash_result.pack()

# Start the main loop
app.mainloop()