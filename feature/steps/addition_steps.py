from behave import *
from compare import *

from helpers.Operators import Operators


#@use_step_matcher("parse")

@given("I have the calculator opened")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("I enter a first number: {first:d}")
def step_impl(context, first):
    """
    :param first:
    :type context: behave.runner.Context
    """
    context.first = first


@step("I press the {operator} button")
def step_impl(context, operator):
    """
    :param operator:
    :type context: behave.runner.Context
    """
    context.operator = operator


@step("I enter a second number: {second:d}")
def step_impl(context, second):
    """
    :param second:
    :type context: behave.runner.Context
    """
    context.second = second


@step("I press = button to performance the operation")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.result = Operators.perform_operation(context.first, context.second, context.operator)


@then('I should have {result:d} as a sum')
def step_impl(context, result):
    expect(context.result).to_equal(result)
