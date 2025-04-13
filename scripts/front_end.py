import tkinter as tk
from tkinter import messagebox
import json

# Load the pairings from the JSON file
try:
    with open("./data/name_picker.json", "r") as f:
        pairings = json.load(f)
except FileNotFoundError:
    pairings = {}

# Function to reveal the Secret Santa assignment
def reveal_assignment():
    name = name_entry.get().strip()
    if name in pairings:
        recipient = pairings[name]
        messagebox.showinfo("🎁 Your Secret Santa", f"You are the Secret Santa for {recipient}!")
    else:
        messagebox.showerror("Name not found", "Sorry, your name was not found in the list.")

# Set up the GUI window
root = tk.Tk()
root.title("Secret Santa Reveal")
root.geometry("400x200")

# Widgets
title_label = tk.Label(root, text="🎄 Secret Santa Reveal 🎄", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

name_label = tk.Label(root, text="Enter your name:")
name_label.pack()

name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

reveal_button = tk.Button(root, text="Reveal", command=reveal_assignment)
reveal_button.pack(pady=10)

# Run the GUI
root.mainloop()
