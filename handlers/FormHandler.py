class FormHandler:

    @staticmethod
    def verify_input_valid(input_type, value):
        if input_type['field'] == 'text':
            return True

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






