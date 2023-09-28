"""Main"""
from datetime import datetime
from fastapi import FastAPI
from fastapi import status
from fastapi.responses import JSONResponse
from src.client import ClientInvertexto


app = FastAPI()


@app.get("/holidays/")
def get_holidays_route(
    year: int = datetime.now().year, state: str = ""
) -> JSONResponse:
    """Get holidays by year and state"""
    client = ClientInvertexto()
    return JSONResponse(
        content=client.get_holidays(year, state), status_code=status.HTTP_200_OK
    )


@app.get("/validator/")
def get_cpf_validator_route(value: str) -> JSONResponse:
    """Get holidays by year and state"""
    client = ClientInvertexto()
    return JSONResponse(
        content=client.get_cpf_validator(value), status_code=status.HTTP_200_OK
    )
