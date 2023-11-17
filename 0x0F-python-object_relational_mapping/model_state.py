#!/usr/bin/python3
"""class definition of a State
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String
from sqlalchemy import Column

Base = declarative_base()


class State(Base):
    """Sub-class that inherits from Base"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
