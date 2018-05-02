import tkinter as tk
from tkinter import messagebox

from constants.config import Config
from handlers.YamlLoader import YamlLoader
from views.Form import Form


class AppContent(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#CCC", width=500, height=500)
        self.pack(expand=True, fill="both", side="right")

        self.title = tk.Text(self, height=1)
        self.title.pack()

        self.form = Form(self)

    def load(self, key, desc):
        data, errors = YamlLoader.load_file("{}/model/".format(Config.CONFIG_ROOT_PATH), "Def{}.yml".format(key))

        if errors:
            messagebox.showinfo('The following errors have occurred', '\n'.join(errors))

        self.title.delete("1.0", tk.END)
        self.title.insert(tk.END, "{}: {}".format(key, desc))

        self.form.populate_with(key, data)

