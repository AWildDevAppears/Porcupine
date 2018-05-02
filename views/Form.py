import tkinter as tk

from handlers.FormHandler import FormHandler
from handlers.InputLoader import InputLoader
from handlers.YamlLoader import YamlLoader


class Form(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.bundle = {}
        self.save_button = {}
        self.title = ''

    def populate_with(self, title, data):
        self.title = title

        if self.save_button:
            self.save_button.destroy()

        for k in self.bundle:
            self.bundle[k]['label'].destroy()
            self.bundle[k]['input'].destroy()

        for k in data:
            self.bundle[k] = {
                'label': tk.Label(self, text=k)
            }

            self.bundle[k]['label'].pack(fill=tk.BOTH)

            self.create_field(k, InputLoader.get_input_by_reference(data[k]))

        self.save_button = tk.Button(self, text='Save', command=self.save_form)
        self.save_button.pack()

    def create_field(self, k, field):
        if field['field'] == 'text' or field['field'] == 'numerical':
            self.bundle[k]['input'] = tk.Entry(self)
            self.bundle[k]['input'].pack(fill=tk.BOTH)
        elif field['field'] == 'radio':
            self.create_dropdown_from_options(k, field['modifier'].split(', '))
        elif field['field'] == 'type':
            types, errors = YamlLoader.get_type(field['reference'])
            if errors:
                tk.messagebox.showinfo('The following errors have occurred', '\n'.join(errors))
                return

            self.create_dropdown_from_options(k, list(map(lambda t: t['name'], types)))

    def save_form(self):
        FormHandler.save_form(self.title, self.bundle)

    def create_dropdown_from_options(self, k, options):
        variable = tk.StringVar(self)
        variable.set(options[0])  # default value

        self.bundle[k]['input'] = tk.OptionMenu(self, variable, *options)
        self.bundle[k]['input'].pack()
