import pytest
from app.models.calculation import Division, Addition


def test_division_by_zero():
    obj = Division(a=10, b=0)
    with pytest.raises(ValueError):
        obj.compute()


def test_division_none_safe():
    obj = Division(a=10, b=None)
    with pytest.raises(ValueError):
        obj.compute()


def test_addition_none_input():
    obj = Addition(a=None, b=5)
    with pytest.raises(ValueError):
        obj.compute()


def test_addition_negative_values():
    obj = Addition(a=-5, b=-10)
    assert obj.compute() == -15