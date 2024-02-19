#!/usr/bin/python
"""
Set up Alchemy to acccess MySQL database
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """create a State class that will be mapped to database"""

    __tablename__ = "states"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
