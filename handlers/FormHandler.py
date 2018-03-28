class FormHandler:
    @staticmethod
    def verify_input_valid(input_def, value):
        if input_def['field'] == 'text':
            return True

        if FormHandler.is_number(value):
            if '.' in value and input_def['field'] == 'numerical' and input_def['modifier']:
                return True
            if input_def['field'] == 'numerical':
                return True
            return False
        
        if input_def['field'] == 'boolean':
            return isinstance(value, bool)

    @staticmethod
    def is_number(value):
        try:
            float(value)
            return True
        except ValueError:
            return False






