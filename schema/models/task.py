from sqlalchemy import Column, Integer, String
from schema.models.base import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    subtitle = Column(String)
    name = Column(String)
    description = Column(String)
