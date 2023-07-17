import datetime

from fastapi import (
    FastAPI,
    File,
    UploadFile,
    status,
)

from src.schemas import (
    InsuranceResponse,
    RateCreatePydantic,
    RateListPydantic,
)
from src.service import (
    calculate_insurance,
    create_rate,
    get_rate_all,
    save_data_from_file,
)


app = FastAPI()


@app.get('/calculate_insurance/',
         response_model=InsuranceResponse,
         status_code=status.HTTP_200_OK)
async def get_rate(date: datetime.date, price: int, cargo_type: str):
    return await calculate_insurance(date=date, price=price, cargo_type=cargo_type)


@app.get('/rates/',
         response_model=RateListPydantic,
         status_code=status.HTTP_200_OK)
async def get_list_of_rate():
    return await get_rate_all()


@app.post('/upload_file_tariff/',
          response_model=RateListPydantic,
          status_code=status.HTTP_201_CREATED)
async def upload_file_with_rates(data: UploadFile = File(...)):
    return await save_data_from_file(data)


@app.post('/upload_tariff/',
          response_model=RateListPydantic,
          status_code=status.HTTP_201_CREATED)
async def load_rates(data: list[RateCreatePydantic]):
    return await create_rate(data)
