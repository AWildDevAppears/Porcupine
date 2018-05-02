from tkinter import filedialog
from yaml import load


class Config:
    CONFIG_ROOT_PATH = './Dataset'
    CONFIG_OUT_PATH = './out'

    @staticmethod
    def load_config():
        filename = filedialog.askopenfile(filetypes=('Config file', '*.yml'))

        if filename:
            config = load(open(filename, 'r'))
            if 'CONFIG_ROOT_PATH' in config:
                Config.CONFIG_ROOT_PATH = config['CONFIG_ROOT_PATH']
            if 'CONFIG_OUT_PATH' in config:
                Config.CONFIG_OUT_PATH = config['CONFIG_OUT_PATH']
