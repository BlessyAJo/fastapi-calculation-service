from pydantic import BaseModel, Field, field_validator
from typing import Literal
from uuid import UUID


# -------------------------
# CREATE SCHEMA
# -------------------------
class CalculationCreate(BaseModel):
    a: float = Field(..., description="First number")
    b: float = Field(..., description="Second number")

    type: Literal["addition", "subtraction", "multiplication", "division"]


# -------------------------
# RESPONSE SCHEMA
# -------------------------
class CalculationRead(BaseModel):
    id: UUID
    user_id: UUID | None = None

    a: float
    b: float
    type: Literal["addition", "subtraction", "multiplication", "division"]
    result: float | None = None

    class Config:
        from_attributes = True