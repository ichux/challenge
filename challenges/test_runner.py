#!/usr/bin/env python3

import cProfile
import os
import os.path

import pytest
from test_cases import fixtures, import_current_test


def get_solutions():
    solutions_out = {}
    solutions_dir = os.path.join(os.getcwd(), "solutions")
    problem_types = [
        x
        for x in os.listdir(solutions_dir)
        if os.path.isdir(os.path.join(solutions_dir, x)) and "__" not in x
    ]
    for each_problem in problem_types:
        solutions_out[each_problem] = []
        current_problem_path = os.path.join(solutions_dir, each_problem)
        all_solutions = [x for x in os.listdir(current_problem_path) if "__" not in x]
        for each_solution in all_solutions:
            solutions_out[each_problem].append(
                {
                    "shortname": each_solution.strip(".py"),
                    "full_path": os.path.join(current_problem_path, each_solution),
                }
            )
    return solutions_out


def run_tests(target_solutions):
    test_dir = os.path.join(os.getcwd(), "test_cases")
    for each_problem, solution_set in target_solutions.items():
        test_file = os.path.join(test_dir, f"test_{each_problem}.py")
        print(
            f"\n\n****************************** Running {test_file} for {each_problem} solutions...\n\n"
        )
        for each_solution in solution_set:
            print(
                f"\n\n****************************** Running tests for {each_solution['shortname']}...\n\n"
            )
            os.environ["CURRENT_NEBX_TEST"] = ".".join(
                [each_problem, each_solution["shortname"]]
            )
            return_code = pytest.main(["--profile", "-vv", test_file])
            if return_code == 0:
                print(
                    f"\n\n****************************** {each_solution['shortname']} was SUCCESSFUL, profiling.....\n\n"
                )
                solution_module = import_current_test()
                current_test_data = getattr(fixtures, f"{each_problem.upper()}_DATA")
                with cProfile.Profile() as pr:
                    for each_input, _ in current_test_data:
                        solution_module.solution(*each_input)
                    pr.print_stats()
            else:
                print(
                    f"\n\n****************************** {each_solution['shortname']} FAILED tests.\n\n"
                )
    print("\n****************************** Test cases complete.")


if __name__ == "__main__":
    TARGET_SOLUTIONS = get_solutions()
    run_tests(TARGET_SOLUTIONS)
