#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys


if __name__ == "__main__":
    username, password, db_name = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    # create all tables in the database
    Base.metadata.create_all(engine)

    # create a session
    Session = sessionmaker(engine)
    session = Session()

    # create a new state California with city San Francisco
    california = State(name="California")
    california.cities.append(City(name="San Francisco"))

    # add State and City to the session
    session.add(california)

    # commit changes to the database
    session.commit()

    # close the active session
    session.close()
