from challenges.test_cases import import_current_test
from challenges.test_cases.fixtures import MAXIMAL_SUBSTRING_DATA


def test_longest_parentheses():
    test_module = import_current_test()
    for test_input, expected_output in MAXIMAL_SUBSTRING_DATA:
        assert test_module.solution(*test_input) == expected_output
