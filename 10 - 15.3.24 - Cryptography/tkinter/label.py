import tkinter as tk

courses = ['C++', 'Python', 'Java', 'React', 'Node', 'Angular']

# 'grid' layout - Display a simple label using the 'grid' layout
# 'width' is the number of characters (avg. number of pixels per character)
for c in courses:
    tk.Label(text=c, width=15).grid(column=0)
    tk.Label(text='Course', relief=tk.SUNKEN, width=15).grid(column=1)

# 'pack' layout - Display a simple label using the 'pack' concept
# label = tk.Label(text='Tomer Sagi', width=15)
# label.pack()

tk.mainloop()