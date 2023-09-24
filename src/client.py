"""Client to access external API"""
import json
import requests
from fastapi.exceptions import HTTPException
from holidays.src.config import INVERTEXT_HOLIDAY_URL, INVERTEXT_KEY, INVERTEXT_LOCATION_URL


class ClientInvertexto():
    """Client for external API"""

    def get_holidays(self, year: int, state: str = None) -> json:
        """Get holidays from Invertexto"""
        params = {
            "token": INVERTEXT_KEY,
        }

        if state:
            params.update({"state": state})

        reponse = requests.get(url=f"{INVERTEXT_HOLIDAY_URL}{year}/", params=params, timeout=500)
        if reponse.status_code != 200:
            raise HTTPException(status_code=reponse.status_code, detail=reponse.json())

        return reponse.json()

    def get_location(self, ip_location: str) -> json:
        """Get ip loca from Invertexto"""
        params = {
            "token": INVERTEXT_KEY,
        }

        reponse = requests.get(
            url=f"{INVERTEXT_LOCATION_URL}{ip_location}/", params=params, timeout=500
        )
        if reponse.status_code != 200:
            raise HTTPException(status_code=reponse.status_code, detail=reponse.json())

        return reponse.json()
