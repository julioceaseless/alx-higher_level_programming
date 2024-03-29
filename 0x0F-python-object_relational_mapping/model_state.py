#!/usr/bin/python3
"""
Set up sql table with sqlalchemy
"""


from sqlalchemy import Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """create a State class that will be mapped to database"""

    __tablename__ = "states"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
