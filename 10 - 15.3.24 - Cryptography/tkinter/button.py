import tkinter as tk


def on_click():
    print('Button Clicked')


root = tk.Tk()
tk.Button(root, text="Click Me", command=on_click).grid(column=0)

root.mainloop()
