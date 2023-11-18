#!/usr/bin/python3
"""class definition of a State
"""
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from relationship_city import Base


class State(Base):
    """Sub-class State that inherits from Base"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    cities = relationship("City", backref="state", cascade="all, delete")
