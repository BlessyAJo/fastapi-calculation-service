import pytest
from app.models.calculation import Addition, Subtraction, Multiplication, Division


@pytest.mark.parametrize("cls,a,b,expected", [
    (Addition, 2, 3, 5),
    (Subtraction, 5, 3, 2),
    (Multiplication, 2, 3, 6),
    (Division, 10, 2, 5),
])
def test_compute_operations(cls, a, b, expected):
    obj = cls(a=a, b=b)
    assert obj.compute() == expected


def test_division_by_zero():
    obj = Division(a=10, b=0)
    with pytest.raises(ValueError):
        obj.compute()