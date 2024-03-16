import tkinter as tk


def on_click():
    # 1. Update 'counter' (make sure it's the 'global' counter)
    global counter
    counter += 1

    # 2. Re-set the counter variable into the widget
    label.configure(text=counter)


# 1. Initiate the TK app by calling the constructor
root = tk.Tk()

# 2. Set the global variables
counter = 0

# 3. Create the UI widgets
label = tk.Label(root, width=5, text=counter)
label.grid(column=0)

tk.Button(root, text="Click Me", command=on_click).grid(column=0)

# 4. Display the UI component and go into an infinite loop
root.mainloop()
