#!/usr/bin/python3
"""class definition of a City
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, ForeignKey

Base = declarative_base()


class City(Base):
    """Sub-class that inherits from Base"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states_id'))
