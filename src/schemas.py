import datetime
import decimal

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from models import Rate


RatePydantic = pydantic_model_creator(Rate)


class InsuranceResponse(BaseModel):
    insurance_coast: float


class RateCreatePydantic(BaseModel):
    cargo_type: str
    date: datetime.date
    rate: decimal.Decimal


class RateListPydantic(BaseModel):
    rates: list[RatePydantic]


class RateRequest(BaseModel):
    cargo_type: str
    rate: decimal.Decimal


class RateRequestModel(BaseModel):
    _: dict[datetime.date, list[RateRequest]]
