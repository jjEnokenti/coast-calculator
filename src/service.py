import datetime
import json

from fastapi import (
    HTTPException,
    UploadFile,
    status,
)
from tortoise import transactions
from tortoise.exceptions import DoesNotExist

from src.models import Rate
from src.schemas import (
    InsuranceResponse,
    RateCreatePydantic,
    RateFileRequest,
    RateListPydantic,
    RatePydantic,
)


async def get_rate_all() -> RateListPydantic:
    return RateListPydantic(rates=await Rate.all())


async def _get_rate_by_date_and_cargo_type(
        date: datetime.date, cargo_type: str) -> Rate:
    try:
        return await Rate.filter(
            date=date, cargo_type=cargo_type).first()

    except DoesNotExist as err:
        raise HTTPException(
            detail=err.args[0], status_code=status.HTTP_404_NOT_FOUND)


async def calculate_insurance(
        date: datetime.date,
        price: int,
        cargo_type: str) -> InsuranceResponse | HTTPException:
    rate = await _get_rate_by_date_and_cargo_type(
        date=date,
        cargo_type=cargo_type
    )
    if rate:
        return InsuranceResponse(insurance_coast=rate.rate * price)

    raise HTTPException(detail='rate not found!', status_code=status.HTTP_404_NOT_FOUND)


async def create_rate(data: list[RatePydantic]) -> RateListPydantic:
    try:
        async with transactions.in_transaction():
            rates = []

            for item in data:
                rate, created = await Rate.get_or_create(
                    date=item.date,
                    cargo_type=item.cargo_type,
                    defaults={
                        'rate': item.rate})

                if not created:
                    rate.rate = item.rate
                    await rate.save()

                rates.append(rate)

        return RateListPydantic(rates=rates)

    except Exception as err:
        raise HTTPException(
            detail=err, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


async def prepare_to_save_data(data: RateFileRequest) -> RateListPydantic:
    try:
        new_rates = []

        for item in data:
            for rate in data[item]:
                new_rate = RateCreatePydantic(date=item, rate=rate['rate'],
                                              cargo_type=rate['cargo_type'])
                new_rates.append(new_rate)

    except Exception as err:
        raise Exception(err)

    return await create_rate(new_rates)


async def save_data_from_file(data: UploadFile) -> RateListPydantic:
    try:
        data = json.loads(await data.read())
    except Exception as err:
        raise HTTPException(
            detail=err.args[0],
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    try:
        return await prepare_to_save_data(data)

    except Exception:
        raise HTTPException(detail='Not valid data', status_code=status.HTTP_400_BAD_REQUEST)
