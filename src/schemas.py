"""Service schemas"""
from datetime import date
from pydantic import BaseModel


class ResponseInvertexto(BaseModel):
    """Reponse external API schema"""

    date: date
    name: str
    type: str
    level: str

