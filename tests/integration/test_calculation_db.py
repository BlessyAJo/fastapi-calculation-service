import pytest
from app.models.calculation import Calculation
from tests.conftest import db


# -------------------------
# INTEGRATION TEST
# -------------------------
def test_insert_calculation(db, test_user):

    calc = Calculation(
        a=10,
        b=5,
        type="addition",
        result=15,
        user_id=test_user.id 
    )

    db.add(calc)
    db.commit()

    stored = db.query(Calculation).filter_by(id=calc.id).first()

    assert stored.user_id == test_user.id
    assert stored.result == 15

def test_division_by_zero():
    from app.models.calculation import Division

    obj = Division(a=10, b=0)

    with pytest.raises(ValueError):
        obj.compute()


def test_calculation_object_fields():
    calc = Calculation(
        a=10,
        b=5,
        type="addition",
        result=15
    )

    assert calc.a == 10
    assert calc.b == 5
    assert calc.result == 15

def test_insert_multiple_records(db, test_user):
    c1 = Calculation(a=10, b=5, type="addition", result=15, user_id=test_user.id)
    c2 = Calculation(a=20, b=2, type="division", result=10, user_id=test_user.id)

    db.add_all([c1, c2])
    db.commit()

    results = db.query(Calculation).all()

    assert len(results) >= 2


def test_invalid_user_id(db):
    calc = Calculation(
        a=10,
        b=5,
        type="addition",
        result=15,
        user_id="invalid-uuid"
    )

    db.add(calc)

    with pytest.raises(Exception):
        db.commit()