# Description: This file contains the test functions for the example_functions.py file
# Test for example functions
import pytest
# test for my_adder function
def test_my_adder():
    """
    Test the my_adder function.
    args: a, b, c
    return: The output of my_adder is equal to the expected sum of a, b, and c.

    """
    from example_functions import my_adder
    assert my_adder(1, 2, 3) == 6
    assert my_adder

# test for my_thermo_stat function
def test_my_thermo_stgitat():
    """
    Test the my_thermo_stat function.
    args: temp, desired_temp
    return: The output of my_thermo_stat is equal to the expected status.

    """
    from example_functions import my_thermo_stat
    assert my_thermo_stat(69, 75) == 'Heat'
    assert my_thermo_stat(81, 75) == 'AC'
    assert my_thermo_stat(75, 75) == 'off'

# test for have_digits function
def test_have_digits():
    """
    Test the have_digits function.
    args: s
    return: The output of have_digits is equal to 1 if there are digits in s, 0 otherwise.
    
    """
    from example_functions import have_digits
    assert have_digits('abc123') == 1
    