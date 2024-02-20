#!/usr/bin/python3
"""
Set up sql table named city with sqlalchemy
"""


from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """create a State class that will be mapped to database"""

    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __repr__(self):
        return f'{self.id}: {self.name}'
