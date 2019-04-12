def before_all(context):
    print("******before******")
    context.test = "+++++Hi AT-09+++++"


def before_scenario(context, scenario):
    print("******before_scenario******")

    if "regresion" in scenario.tags:
        print("***********", scenario.tags, "***********")
    context.test = "+++++Hi scenarioAT-09+++++"


def before_scenario(context, scenario):
    print("******before_scenarioAT09******")

    if "AT09" in scenario.tags:
        print("***********", scenario.tags, "***********")
    context.test = "+++++Hi scenarioAT-09+++++"


def after_scenario(context, scenario):
    print("******after_scenario******")
