#!/usr/bin/python3
"""Map cities to a declarative model that shares the State metadata."""
from sqlalchemy import Column, ForeignKey, Integer, String

from model_state import Base


class City(Base):
    """Represent a city with a name and a foreign key to its state."""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
