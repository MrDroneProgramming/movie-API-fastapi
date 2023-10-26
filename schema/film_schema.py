from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FilmSchema(BaseModel):
    film_id: Optional[int]
    title: str
    created_on: datetime
    runtime: int
    director: str
    genre: str