from types import SimpleNamespace


def run_tests(request_node, response):
    all_passed = []
    for test in request_node.tests:
        name = test["name"]
        test = test["test"]
        passed = eval(test)
        all_passed.append(passed)
        print(f"\n{request_node.id} -> {name}: {passed}\n")

    report = {"passed": all(all_passed)}
    return SimpleNamespace(**report)
