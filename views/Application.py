import tkinter as tk
from tkinter import messagebox

from constants.config import Config
from handlers.YamlLoader import YamlLoader
from views.AppContent import AppContent
from views.Sidemenu import Sidemenu


class Application(tk.Frame):
    def __init__(self, master=tk.Tk()):
        super().__init__(master)
        self.pack()

        self.sidemenu = Sidemenu(self)
        self.content = AppContent(self)

        items, errors = YamlLoader.load_definitions_file(Config.CONFIG_ROOT_PATH, 'Definitions.yml')

        if errors:
            messagebox.showinfo('The following errors have occurred', '\n'.join(errors))

        self.sidemenu.append_items(items)

    def load_list_for(self, key, desc):
        self.content.load(key, desc)

