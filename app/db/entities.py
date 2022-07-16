import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()

class StatsModel(Base):
    __tablename__ = 'stats'
    id = Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    timestamp = Column('timestamp', DateTime)
    stats = Column('stats', JSON)