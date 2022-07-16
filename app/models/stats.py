from datetime import date, datetime
from pstats import Stats
from typing import List
from uuid import UUID
from pydantic import BaseModel, Json


class NewStats(BaseModel):
    timestamp: datetime
    stats: dict

class Stats(NewStats):
    id: UUID
    class Config:
        orm_mode = True

class ResponseModel(BaseModel):
    result: Stats
    status: int = 200

class ResponseListModel(BaseModel):
    result: List[Stats]
    status: int = 200
