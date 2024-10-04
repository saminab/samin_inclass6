# Description: This file contains the test functions for the example_functions.py file
# Test for example functions
import pytest
# test for my_adder function
def test_my_adder():
    from example_functions import my_adder
    assert my_adder(1, 2, 3) == 6
    assert my_adder

# test for my_thermo_stat function
def test_my_thermo_stat():
    from example_functions import my_thermo_stat
    assert my_thermo_stat(69, 75) == 'Heat'
    assert my_thermo_stat(81, 75) == 'AC'
    assert my_thermo_stat(75, 75) == 'off'

# test for have_digits function
def test_have_digits():
    from example_functions import have_digits
    assert have_digits('abc123') == 1
    