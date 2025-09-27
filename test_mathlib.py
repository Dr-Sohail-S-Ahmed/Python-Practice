# (Check out "python unit testing.py" first + see also Adv Python in Programming.xlsx)

import mathlib
import pytest

@pytest.mark.skip(reason = "I don't know")      # To skip the test + reason is optional
def test_calc_total():
    total = mathlib.calc_total(4,5)
    assert total == 9       # "assert" checks if condition is True, program continues but if False, AssertionError is raised

def test_calc_multiply():
    result = mathlib.calc_multiply(10,5)
    assert result == 50

@pytest.mark.windows        # test can be tagged such that only the tagged ones are run + here "windows" & "mac" before are user defined tags
def test_windows_1():
    assert True

@pytest.mark.windows
def test_windows_2():
    assert True

@pytest.mark.mac
def test_mac_1():
    assert True

@pytest.mark.mac
def test_mac_2():
    assert True