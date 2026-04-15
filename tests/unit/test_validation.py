import pytest
from app.schemas.calculation import CalculationCreate, CalculationRead
from pydantic import ValidationError
from uuid import uuid4


def test_valid_schema():
    data = CalculationCreate(
        a=10,
        b=5,
        type="addition"
    )
    assert data.a == 10


def test_invalid_type():
    with pytest.raises(ValidationError):
        CalculationCreate(
            a=10,
            b=5,
            type="invalid_type"
        )


def test_none_value():
    with pytest.raises(ValidationError):
        CalculationCreate(
            a=None,
            b=5,
            type="addition"
        )
def test_missing_field():
    with pytest.raises(ValidationError):
        CalculationCreate(a=10, type="addition")


def test_negative_values_allowed():
    obj = CalculationCreate(a=-10, b=-5, type="addition")
    assert obj.a == -10

# -------------------------
# VALID CREATE SCHEMA
# -------------------------
def test_calculation_create_valid():
    data = CalculationCreate(
        a=10,
        b=5,
        type="addition"
    )

    assert data.a == 10
    assert data.b == 5
    assert data.type == "addition"


# -------------------------
# INVALID TYPE
# -------------------------
def test_calculation_create_invalid_type():
    with pytest.raises(ValidationError):
        CalculationCreate(
            a=10,
            b=5,
            type="invalid_operation"
        )


# -------------------------
# MISSING FIELD
# -------------------------
def test_calculation_create_missing_field():
    with pytest.raises(ValidationError):
        CalculationCreate(
            a=10,
            type="addition"
        )


# -------------------------
# RESPONSE SCHEMA VALIDATION
# -------------------------
def test_calculation_read_valid():
    data = CalculationRead(
        id=uuid4(),
        user_id=uuid4(),
        a=10,
        b=5,
        type="addition",
        result=15
    )

    assert data.result == 15
    assert data.type == "addition"


# -------------------------
# OPTIONAL FIELD TEST
# -------------------------
def test_calculation_read_optional_user_id():
    data = CalculationRead(
        id=uuid4(),
        a=10,
        b=5,
        type="addition",
        result=15
    )

    assert data.user_id is None