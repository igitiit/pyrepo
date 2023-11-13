import tkinter as tk
from crud import CRUD

class App:
    def __init__(self, master):
        self.master = master
        self.crud = CRUD("database.db")

        # Create GUI elements
        self.label = tk.Label(self.master, text="Enter data:")
        self.label.pack()

        self.entry1 = tk.Entry(self.master)
        self.entry1.pack()

        self.entry2 = tk.Entry(self.master)
        self.entry2.pack()

        self.button_create = tk.Button(self.master, text="Create", command=self.create)
        self.button_create.pack()

        self.button_read = tk.Button(self.master, text="Read", command=self.read)
        self.button_read.pack()

        self.button_update = tk.Button(self.master, text="Update", command=self.update)
        self.button_update.pack()

        self.button_delete = tk.Button(self.master, text="Delete", command=self.delete)
        self.button_delete.pack()

    def create(self):
        data = (self.entry1.get(), self.entry2.get())
        self.crud.create(data)

    def read(self):
        id = self.entry1.get()
        data = self.crud.read(id)
        self.entry2.delete(0, tk.END)
        self.entry2.insert(0, data[1])

    def update(self):
        id = self.entry1.get()
        data = (self.entry2.get(),)
        self.crud.update(id, data)

    def delete(self):
        id = self.entry1.get()
        self.crud.delete(id)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()