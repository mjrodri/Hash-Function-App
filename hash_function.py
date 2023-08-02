import tkinter as tk
from tkinter import ttk
import hashlib

def compute_hash():
    algorithm = hash_algorithm.get()
    data = entry_data.get()

    if algorithm == "MD5":
        hash_func = hashlib.md5()
    elif algorithm == "SHA-1":
        hash_func = hashlib.sha1()
    elif algorithm == "SHA-256":
        hash_func = hashlib.sha256()
    else:
        return
    
    hash_func.update(data.encode('utf-8'))
    hashed_data = hash_func.hexdigest()

    label_hash_result.config(text=f"{algorithm} Hash: {hashed_data}")

# Create the main application window
app = tk.Tk()
app.title("Hash Function")

# Add elements
label_instruction = tk.Label(app, text="Enter your data :")
label_instruction.pack()

entry_data = tk.Entry(app)
entry_data.pack()

hash_algorithm = ttk.Combobox(app, values=["MD5", "SHA-1", "SHA-256"])
hash_algorithm.set("Select")
hash_algorithm.pack()

button_compute = tk.Button(app, text="Compute Hash", command = compute_hash)
button_compute.pack() 

label_hash_result = tk.Label(app, text="")
label_hash_result.pack()

# Start the main loop
app.mainloop()