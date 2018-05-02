from pathlib import Path
from yaml import load

from constants.config import Config


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

        if '_extends' in data:
            key = data['_extends']
            d, e = YamlLoader.load_file('{}/abstract'.format(Config.CONFIG_ROOT_PATH), 'Abs{}.yml'.format(key))
            data = {**data, **d}
            errors = errors + e
            del data['_extends']

        return data, errors

    @staticmethod
    def load_definitions_file(path, name):
        data, errors = YamlLoader.load_file(path, name)

        if data:
            for k in data:
                if data[k] is None or 'desc' not in data[k]:
                    errors.append('Cannot load definitions, description not found for {}'.format(k))
                if data[k] is None or 'def' not in data[k]:
                    errors.append('Cannot load definitions, model not found for {}'.format(k))
                elif 'def' in data[k] and not Path('{}/model/{}.yml'.format(path, data[k]['def'])).is_file():
                    errors.append('Cannot load definitions, missing model file for {}'.format(k))

        return data, errors

    @staticmethod
    def get_type(reference):
        data, errors = YamlLoader.load_file('{}/types'.format(Config.CONFIG_ROOT_PATH), '{}.yml'.format(reference))

        if data:
            for k in data:
                if 'name' not in k:
                    errors.append('Cannot get name for field in {} at index {}'.format(reference, k))

        return data, errors

