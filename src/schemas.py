import datetime
import decimal

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from models import Rate


RatePydantic = pydantic_model_creator(Rate)


class InsuranceResponse(BaseModel):
    """Insurance response schema."""
    insurance_coast: float


class RateCreatePydantic(BaseModel):
    """New rate create schema."""
    cargo_type: str
    date: datetime.date
    rate: decimal.Decimal


class RateListPydantic(BaseModel):
    """List fo rates schema."""
    rates: list[RatePydantic]


class RateRequest(BaseModel):
    """Schema for file data serializing."""
    cargo_type: str
    rate: decimal.Decimal


class RateFileRequest(BaseModel):
    """Schema for upload data from file."""
    _: dict[datetime.date, list[RateRequest]]
