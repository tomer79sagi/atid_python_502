from tkinter import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(fill=BOTH, expand=1)
        self.counter = 0

        self.text = Label(self, text="Just do it")
        self.text.grid(row=0, column=0)

        self.button = Button(self, text="Increment Counter", command=self.update_label)
        self.button.grid(row=0, column=1)

        self.entry = Entry(self)
        self.entry.grid(row=1, column=0)

        self.button = Button(self, text="Reset Counter", command=self.reset_counter)
        self.button.grid(row=1, column=1)

    def update_label(self):
        self.counter += 1
        self.text.config(text=f"Clicked: {self.counter} times")

    def reset_counter(self):
        self.counter = self.entry.get()
        self.text.config(text=f"Clicked: {self.counter} times")


root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.geometry("200x200")
root.mainloop()