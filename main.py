from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal
import logging

from app.factory.calculation_factory import CalculationFactory
from app.database import Base, engine
from app.models import calculation, user  # important import

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Calculation Service")

class CalculationRequest(BaseModel):
    a: float
    b: float

    type: Literal["addition", "subtraction", "multiplication", "division"]


class CalculationResponse(BaseModel):
    result: float


@app.get("/")
def root():
    return {
        "message": "Calculation API is running",
        "endpoints": ["/calculate"]
    }


@app.post("/calculate", response_model=CalculationResponse)
def calculate(req: CalculationRequest):

    try:
        operation = CalculationFactory.create(req.a, req.b, req.type)
        result = operation.compute()

        logger.info(f"logg: {req.type}: {req.a}, {req.b} = {result}")

        return CalculationResponse(result=result)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))