import traceback
from pprint import pformat

import pandas as pd

from database import engine
from queries import *


def check(name, observed, expected):

    p_observed = pformat(observed)
    p_expected = pformat(expected)

    correct = observed == expected

    if not correct:
        print(
            f"Case Wrong! | For {name}: Expected={p_expected}, Observed={p_observed}."
        )
    else:
        print(
            f"Case Correct! | For {name}: Expected={p_expected}, Observed={p_observed}."
        )

    return correct


def grade_1():

    print("*" * 50)
    print("PROBLEM 1")

    try:

        df = pd.read_sql_query(query_1, engine)

        # case 1
        observed = len(df)
        expected = 1
        case_1_correct = check("num_rows", observed, expected)

        # case 2
        observed = df.loc[0, "count"]
        expected = 9299
        case_2_correct = check("count", observed, expected)

        all_cases_correct = all([case_1_correct, case_2_correct])

        if all_cases_correct:
            print("PROBLEM CORRECT!")
        else:
            print("PROBLEM INCORRECT!")

        return all_cases_correct

    except Exception as e:
        print("An Error has Occurred while grading PROBLEM:")
        traceback.print_exc()
        print("PROBLEM INCORRECT!")
        return False


def grade_2():

    print("*" * 50)
    print("PROBLEM 2")

    try:

        df = pd.read_sql_query(query_2, engine)

        # case 1
        observed = len(df)
        expected = 1
        case_1_correct = check("num_rows", observed, expected)

        # case 2
        observed = df.loc[0, "count"]
        expected = 9305
        case_2_correct = check("count", observed, expected)

        all_cases_correct = all([case_1_correct, case_2_correct])

        if all_cases_correct:
            print("PROBLEM CORRECT!")
        else:
            print("PROBLEM INCORRECT!")

        return all_cases_correct

    except Exception as e:
        print("An Error has Occurred while grading PROBLEM:")
        traceback.print_exc()
        print("PROBLEM INCORRECT!")
        return False


def grade_3():

    print("*" * 50)
    print("PROBLEM 3")

    try:

        df = pd.read_sql_query(query_3, engine)

        # case 1
        observed = len(df)
        expected = 1
        case_1_correct = check("num_rows", observed, expected)

        # case 2
        observed = df.loc[0, "max"]
        expected = 17729020
        case_2_correct = check("max", observed, expected)

        # case 3
        observed = df.loc[0, "min"]
        expected = -3
        case_3_correct = check("min", observed, expected)

        all_cases_correct = all([case_1_correct, case_2_correct, case_3_correct])

        if all_cases_correct:
            print("PROBLEM CORRECT!")
        else:
            print("PROBLEM INCORRECT!")

        return all_cases_correct

    except Exception as e:
        print("An Error has Occurred while grading PROBLEM:")
        traceback.print_exc()
        print("PROBLEM INCORRECT!")

        return False


def grade_4():

    print("*" * 50)
    print("PROBLEM 4")

    try:

        df = pd.read_sql_query(query_4, engine)

        # case 1
        observed = df.iloc[0]["stabr"]
        expected = "CA"
        case_1_correct = check("state_with_most_visits", observed, expected)

        # case 2
        observed = df.set_index("stabr").loc["CA", "visits"]
        expected = 164300175
        case_2_correct = check("CA_num_visits", observed, expected)

        all_cases_correct = all([case_1_correct, case_2_correct])

        if all_cases_correct:
            print("PROBLEM CORRECT!")
        else:
            print("PROBLEM INCORRECT!")

        return all_cases_correct

    except Exception as e:
        print("An Error has Occurred while grading PROBLEM:")
        traceback.print_exc()
        print("PROBLEM INCORRECT!")

        return False


def grade_5():

    print("*" * 50)
    print("PROBLEM 5")

    try:
        df = pd.read_sql_query(query_5, engine)

        # case 1
        observed = len(df)
        expected = 1
        case_1_correct = check("num_rows", observed, expected)

        # case 2
        observed = df.loc[0, "change_in_visits"]
        expected = -165868301
        case_2_correct = check("change", observed, expected)

        all_cases_correct = all([case_1_correct, case_2_correct])

        if all_cases_correct:
            print("PROBLEM CORRECT!")
        else:
            print("PROBLEM INCORRECT!")

        return all_cases_correct

    except Exception as e:
        print("An Error has Occurred while grading PROBLEM:")
        traceback.print_exc()
        print("PROBLEM INCORRECT!")

        return False


def grade_6():

    print("*" * 50)
    print("PROBLEM 6")

    try:
        df = pd.read_sql_query(query_6, engine)

        # case 1
        observed = len(df)
        expected = 1
        case_1_correct = check("num_rows", observed, expected)

        # case 2
        observed = df.loc[0, "change_in_visits"]
        expected = -168155964
        case_2_correct = check("change", observed, expected)

        all_cases_correct = all([case_1_correct, case_2_correct])

        if all_cases_correct:
            print("PROBLEM CORRECT!")
        else:
            print("PROBLEM INCORRECT!")

        return all_cases_correct

    except Exception as e:
        print("An Error has Occurred while grading PROBLEM:")
        traceback.print_exc()
        print("PROBLEM INCORRECT!")

        return False


if __name__ == "__main__":
    results = [
        grade_1(),
        grade_2(),
        grade_3(),
        grade_4(),
        grade_5(),
        grade_6(),
    ]

    num_correct = sum(results)
    num_problems = len(results)

    print("=" * 100)
    print(f"{num_correct} out of {num_problems} problems")
    print("=" * 100)
