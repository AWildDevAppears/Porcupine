import re


class InputLoader:

    @staticmethod
    def get_input_by_reference(ref):
        modifier = ''
        optional = 'False'
        reference = ''
        multiple = 'False'

        # Handling array types
        if re.match('array<(.*)>', ref) is not None:
            multiple = 'True'
            ref = re.match('array<(.*)>', ref).group(1)
        elif re.match('radio<(.*)>', ref) is not None:
            return {
                'field': 'radio',
                'modifier': re.match('radio<(.*)>', ref).group(1),
                'optional': 'True' if ref[-1] == '?' else 'False',
                'reference': '',
                'multiple': 'False',
            }

        # Handling optional types
        if ref[-1] == '?':
            optional = 'True'
            ref = ref[:-1]

        # Handling reference types
        if ref[0] == '~':
            reference = ref[1:]
            field = 'reference'
        # Handling preset types
        elif ref[0] == '$':
            field = 'type'
            reference = ref[1:]
        # Handling primitive types
        else:
            field = InputLoader.get_field_for(ref)

            if ref == 'float':
                modifier = 'decimal'

        return {
            'field': field,
            'modifier': modifier,
            'optional': optional,
            'reference': reference,
            'multiple': multiple,
        }

    @staticmethod
    def get_field_for(value):
        if value == 'string':
            return 'text'
        elif value == 'int':
            return 'numerical'
        elif value == 'float':
            return 'numerical'
        elif value == 'boolean':
            return 'toggle'


