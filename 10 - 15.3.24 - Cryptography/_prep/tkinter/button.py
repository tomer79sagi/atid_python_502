import tkinter as tk
def update_label():
    global counter
    counter += 1
    label.config(text=f"Clicked: {counter} times")

root = tk.Tk()
counter = 0

label = tk.Label(root, text="Clicked: 0 times")
label.pack()

button = tk.Button(root, text="Click Me", command=update_label)
button.pack()

root.mainloop()




