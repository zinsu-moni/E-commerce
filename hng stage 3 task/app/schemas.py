from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

class ProfileOut(BaseModel):
    id: UUID
    name: str
    gender: str
    gender_probability: float
    age: int
    age_group: str
    country_id: str
    country_name: str
    country_probability: float
    created_at: datetime

    class Config:
        orm_mode = True

class ProfilesResponse(BaseModel):
    status: str
    page: int
    limit: int
    total: int
    data: list[ProfileOut]

class ErrorResponse(BaseModel):
    status: str = "error"
    message: str
