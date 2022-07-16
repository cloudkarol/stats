from uuid import UUID
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from app.models import NewStats
from app.services.base import Base
from app.db.entities import StatsModel


class StatsService(Base):
    def add(session: Session, stats: NewStats):
        obj_data = jsonable_encoder(stats)
        _stats = StatsModel(**obj_data)
        session.add(_stats)
        session.commit()
        session.refresh(_stats)
        return _stats

    def get(session: Session):
        result = session.query(StatsModel).all()
        return result
    
    def get_by_id(session: Session, id: UUID):
        result = session.query(StatsModel).filter(StatsModel.id == id).one_or_none()
        return result