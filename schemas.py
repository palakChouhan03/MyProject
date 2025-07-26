# Milestone 3

from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    age: int = Field(..., ge=0)
    gender: Literal['male', 'female', 'other']
    state: str
    street_address: str
    postal_code: str
    city: str
    country: str
    latitude: float
    longitude: float
    traffic_source: str
    created_at: Optional[datetime] = None

class UserOut(UserCreate):
    id: int

    class Config:
        orm_mode = True
