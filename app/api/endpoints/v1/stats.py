from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services import StatsService
from app.models import NewStats, Stats, ResponseModel, ResponseListModel
from app.db import session

router = APIRouter(
    prefix="/stats",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

def get_session():
    db = session()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def stats(session: Session = Depends(get_session)):
    result = StatsService.get(session=session)
    return ResponseListModel(result=[Stats.from_orm(model) for model in result])

@router.get("/{worker_id}")
def stats(worker_id: UUID, session: Session = Depends(get_session)):
    result = StatsService.get_by_id(session=session, id=worker_id)
    return ResponseModel(result=Stats.from_orm(result))

@router.post("/")
def stats(worker_stats: NewStats, session: Session = Depends(get_session)):
    result = StatsService.add(session=session, stats=worker_stats)
    return ResponseModel(result=Stats.from_orm(result))
