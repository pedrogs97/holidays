"""Main"""
from datetime import datetime
from fastapi import FastAPI
from fastapi import status
from fastapi.responses import JSONResponse
from src.client import ClientInvertexto


app = FastAPI()

@app.get('/holidays/')
def get_holidays_route(year: int = datetime.now().year, state: str = '') -> JSONResponse:
    """Get holidays by year and state"""
    client = ClientInvertexto()
    return JSONResponse(content=client.get_holidays(year, state), status_code=status.HTTP_200_OK)
    

@app.get('/location/')
def get_location_route(ip_location: str) -> JSONResponse:
    """Get holidays by year and state"""
    client = ClientInvertexto()
    return JSONResponse(content=client.get_location(ip_location), status_code=status.HTTP_200_OK)