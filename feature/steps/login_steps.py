from behave import step, use_step_matcher

#use_step_matcher("parse")


# @step('I open the browser at: "{url:w}"')
# def step_impl(context, url):
#     """
#     :type context: behave.runner.Context
#     :type url: str
#     """
#     # raise NotImplementedError(u'STEP: Given I open the browser at: "<url>"')
#     pass
use_step_matcher("re")


@step('I open the browser at: (.*)')
def step_impl(context, url):
    """
    :type context: behave.runner.Context
    :type url: str
    """
    # raise NotImplementedError(u'STEP: Given I open the browser at: "<url>"')
    pass


# @given('I open the browser at: "www.at09.com/login"')
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     # raise NotImplementedError(u'STEP: Given I open the browser at: "www.at09.com/login"')
#     pass

@step("I fill (.*) in Account field")
def step_impl(context, account):
    """
    :type context: behave.runner.Context
    :type account: str
    """
    #raise NotImplementedError(u'STEP: Given I fill <account> in Account field')
    pass


@step("I fill (.*) in Password field")
def step_impl(context, password):
    """
    :type context: behave.runner.Context
    :type password: str
    """
    #raise NotImplementedError(u'STEP: And I fill <password> in Password field')
    pass
