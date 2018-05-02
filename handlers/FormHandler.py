import json

from constants.config import Config
from handlers.JSONLoader import JSONLoader


class FormHandler:

    @staticmethod
    def verify_input_valid(input_type, value):
        if (value is None or value == '') and input_type['optional'] == 'False':
            return False

        if input_type['field'] == 'text':
            return True

        if input_type['field'] == 'reference':
            return FormHandler.verify_reference_exists(
                '{}/model/Def{}'.format(Config.CONFIG_ROOT_PATH, input_type['reference']),
                value,
            )

        if FormHandler.is_number(value):
            if input_type['field'] == 'numerical':
                if '.' in value:
                    return input_type['modifier'] == 'decimal'
                return True
            return False

        if input_type['field'] == 'boolean':
            return isinstance(value, bool)

    @staticmethod
    def is_number(value):
        try:
            float(value)
            return True
        except ValueError:
            return False


    @staticmethod
    def verify_reference_exists(path, reference):
        return reference in JSONLoader.load_json_file(path)

    @staticmethod
    def save_form(form_title, form):
        output = {}

        for k in form:
            print(k)
            output[k] = form[k].get()
            # FormHandler.verify_input_valid(input_types[k], output[k])

        JSONLoader.save_json_file('{}/models/{}.json'.format(Config.CONFIG_OUT_PATH, form_title), output)


