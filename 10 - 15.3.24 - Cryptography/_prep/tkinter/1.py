import tkinter as tk
courses = ['C','C++','Python','Java','Unix','DevOps']
r = ['course']
for c in courses:
    tk.Label(text=c, width=15).grid(column=0)
    tk.Label(text=r, relief=tk.RIDGE, width=15).grid(column=1)
tk.mainloop()