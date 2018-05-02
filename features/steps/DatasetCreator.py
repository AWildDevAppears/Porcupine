from behave import *

from handlers.FormHandler import FormHandler


@given('I have an input of type')
def step_impl(context):
    context.res = {
        'input_type': context.table[0],
    }


@when('I enter "{value}"')
def step_impl(context, value):
    context.res['value'] = value


@then('The form should save')
def step_impl(context):
    if context.res['input_type']['field'] == 'reference':
        assert FormHandler.verify_reference_exists('./features/mock/DefA.json', context.res['value']) is True
        return
    assert FormHandler.verify_input_valid(**context.res) is True


@then('The form should not save')
def step_impl(context):
    if context.res['input_type']['field'] == 'reference':
        assert FormHandler.verify_reference_exists('./features/mock/DefA.json', context.res['value']) is False
        return
    assert FormHandler.verify_input_valid(**context.res) is False
