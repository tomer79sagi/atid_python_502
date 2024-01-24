import tkinter as tk
from tkinter import ttk

# Function to update the text field
def say_hello():
    name = name_entry.get()
    greeting = f"Hello, {name}!"
    greeting_label.config(text=greeting)

# Create the main window
root = tk.Tk()
root.title("Greeting App")
root.geometry("300x150")

# Create a label, entry widget, and button
tk.Label(root, text="Enter your name:").pack(pady=5)
name_entry = ttk.Entry(root)
name_entry.pack(pady=5)

greet_button = ttk.Button(root, text="Greet", command=say_hello)
greet_button.pack(pady=5)

greeting_label = ttk.Label(root, text="")
greeting_label.pack(pady=5)

# Run the application
root.mainloop()