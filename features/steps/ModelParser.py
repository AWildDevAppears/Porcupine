from behave import *

from handlers.InputLoader import InputLoader


@given('I have an input type of "{input_type}"')
def step_impl(context, input_type):
    context.res = {
        'input_type': input_type,
    }


@then('it should evaluate to')
def step_impl(context):
    output = InputLoader.get_input_by_reference(context.res['input_type'])

    for row in context.table:
        assert output['field'] == row['field']
        assert output['modifier'] == row['modifier']
        assert output['optional'] == row['optional']
        assert output['reference'] == row['reference']
        assert output['multiple'] == row['multiple']
