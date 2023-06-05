import os
from importlib import import_module


def import_current_test():
    current_test_file = os.environ["CURRENT_NEBX_TEST"]
    return import_module(f"nebx_challenges.solutions.{current_test_file}")
