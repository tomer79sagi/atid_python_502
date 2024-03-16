from tkinter import *


class App(Frame):
    def __init__(self, tk_obj=None):
        Frame.__init__(self, tk_obj)
        # 2. Set the global variables
        self.counter = 0

        # 3. Create the UI widgets
        self.label = Label(tk_obj, width=5, text=self.counter)
        self.label.grid(row=0, column=0)

        self.btn = Button(tk_obj, text="Click Me", command=self.on_click)
        self.btn.grid(row=0, column=1)

        self.entry = Entry(tk_obj)
        self.entry.grid(row=1, column=0)

        self.btn = Button(tk_obj, text="Display Entry", command=self.handle_entry_change)
        self.btn.grid(row=1, column=1)

    def on_click(self):
        # 1. Update 'counter'
        self.counter += 1

        # 2. Re-set the counter variable into the widget
        self.label.configure(text=self.counter)

    def handle_entry_change(self):
        print(self.entry.get())


# 1. Initiate the TK app by calling the constructor
root = Tk()
app = App(root)  # 'App' main application class
root.wm_title('Counter App')
root.geometry('400x300')

# 4. Display the UI component and go into an infinite loop
root.mainloop()
