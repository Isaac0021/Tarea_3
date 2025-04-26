from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
years = []

class Years(BaseModel):
    year: int
    name: str
