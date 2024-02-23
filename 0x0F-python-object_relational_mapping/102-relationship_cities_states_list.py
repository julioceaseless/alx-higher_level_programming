#!/usr/bin/python3
"""script that lists all City objects from the database hbtn_0e_101_usa"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State


if __name__ == "__main__":
    """run this script only when called directly"""
    username, password, db_name = sys.argv[1:]

    # configure the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # create all tables
    Base.metadata.create_all(engine)

    # create a session
    Session = sessionmaker(engine)
    session = Session()

    # query database
    result = session.query(City).all()

    # print results
    for city in result:
        print(f'{city.id}: {city.name} -> {city.state.name}')
