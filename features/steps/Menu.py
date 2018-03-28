from behave import *

from handlers.YamlLoader import YamlLoader


@given('we have loaded the definitions from "{filename}"')
def step_impl(context, filename):
    definitions, error = YamlLoader.load_definitions_file('./features/mock', filename)

    context.res = {
        'definitions': definitions,
        'error': error,
    }


@then('I should see the following fields')
def step_impl(context):
    for row in context.table:
        name = row['name']
        assert context.res['definitions'][name]['desc'] == row['description']


@then('we should receive the error "{message}"')
def step_impl(context, message):
    assert message in context.res['error']

