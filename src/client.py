"""Client to access external API"""
import json
import requests
from fastapi.exceptions import HTTPException
from src.config import INVERTEXT_HOLIDAY_URL, INVERTEXT_KEY, INVERTEXT_VALIDATION_URL


class ClientInvertexto:
    """Client for external API"""

    def get_holidays(self, year: int, state: str = None) -> json:
        """Get holidays from Invertexto"""
        params = {
            "token": INVERTEXT_KEY,
        }

        if state:
            params.update({"state": state})

        reponse = requests.get(
            url=f"{INVERTEXT_HOLIDAY_URL}{year}/", params=params, timeout=500
        )
        if reponse.status_code != 200:
            raise HTTPException(status_code=reponse.status_code, detail=reponse.json())

        return reponse.json()

    def get_cpf_validator(self, value: str) -> json:
        """Get ip loca from Invertexto"""
        params = {"token": INVERTEXT_KEY, "type": "cpf", "value": value}

        reponse = requests.get(
            url=f"{INVERTEXT_VALIDATION_URL}", params=params, timeout=500
        )
        if reponse.status_code != 200:
            raise HTTPException(status_code=reponse.status_code, detail=reponse.json())

        return reponse.json()
