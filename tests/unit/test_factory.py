import pytest
from app.factory.calculation_factory import CalculationFactory
from app.models.calculation import Calculation, Addition, Subtraction, Multiplication, Division


@pytest.mark.parametrize("op_type,expected_class", [
    ("addition", Addition),
    ("subtraction", Subtraction),
    ("multiplication", Multiplication),
    ("division", Division),
])
def test_factory_returns_correct_class(op_type, expected_class):
    obj = CalculationFactory.create(10, 5, op_type)
    assert isinstance(obj, expected_class)


def test_factory_invalid_type():
    with pytest.raises(ValueError):
        CalculationFactory.create(10, 5, "invalid")
def test_factory_case_insensitive():
    obj = CalculationFactory.create(10, 5, "AdDiTiOn")
    assert isinstance(obj, Addition)

def test_chain_execution():
    op = CalculationFactory.create(100, 2, "division")
    assert op.compute() == 50