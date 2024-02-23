#!/usr/bin/python3
"""
script lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys


if __name__ == "__main__":
    """run script only when run directly"""
    user, password, db_name = sys.argv[1:]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, password, db_name),
                           pool_pre_ping=True)
    # create all tables in the database
    Base.metadata.create_all(engine)

    # create a session
    Session = sessionmaker(engine)
    session = Session()

    # query the database
    result = session.query(State).order_by(State.id).all()

    # print each state and its cities
    for state in result:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
