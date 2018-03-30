from pathlib import Path
from yaml import load


class YamlLoader:
    def __init__(self):
        pass

    @staticmethod
    def load_file(path, name):
        errors = []
        data = ''

        filepath = '{}/{}'.format(path, name)

        if not Path(filepath).is_file():
            errors.append('Cannot load file {}, not found'.format(filepath))
            return data, errors

        data = load(open(filepath, 'r'))

        if data is None:
            errors.append('Cannot load file {}, no content'.format(filepath))

        return data, errors

    @staticmethod
    def load_definitions_file(path, name):
        data, errors = YamlLoader.load_file(path, name)

        if data:
            for k in data:
                if 'desc' not in data[k]:
                    errors.append('Cannot load definitions, description not found for {}'.format(k))
                if 'def' not in data[k]:
                    errors.append('Cannot load definitions, model not found for {}'.format(k))
                if 'desc' in data[k] and not Path('{}/handlers/{}.yml'.format(path, data[k]['desc'])).is_file():
                    errors.append('Cannot load definitions, missing model file for {}'.format(k))

        for err in errors:
            print(err)

        return data, errors
