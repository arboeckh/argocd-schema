from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from schema.models.base import Base


class SubTask(Base):
    __tablename__ = "subtasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)

    task = relationship("Task", backref="subtasks")
