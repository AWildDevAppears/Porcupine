import tkinter as tk


class Sidemenu(tk.Frame):
    def __init__(self, master=None):
        self.master = master
        super().__init__(master, width=200, bg='white', height=500, relief='sunken', borderwidth=2)
        self.pack(expand=False, fill='both', side='left', anchor='nw')

        self.list = tk.Listbox(self)
        self.list.pack()

        self.list_items = []

    def append_items(self, items):
        self.list_items = items

        self.list.bind('<<ListboxSelect>>', self.on_select)

        for item in items:
            self.list.insert(tk.END, item)

    def on_select(self, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        key = w.get(index)
        self.master.load_list_for(key, self.list_items[key]['desc'])

