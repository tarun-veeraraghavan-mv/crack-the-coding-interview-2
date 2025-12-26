# poetry run pytest 11_testing/test_testing_functions.py

from testing_functions import get_temp, add, divide
import pytest

def test_get_temp():
    assert get_temp(21) == "hot"
    assert get_temp(20) == "cold"

def test_add():
    assert add(2,3) == 5
    assert add(1,4) != 7
    assert add(7,4) == 11

def test_divide():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10,0)