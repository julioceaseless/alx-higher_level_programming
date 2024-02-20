#!/usr/bin/python3
"""
script lists all State objects from database using sqlalchemy
"""


import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

from model_state import State, Base
from model_city import City


if __name__ == "__main__":
    username, password, db_name = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    """query database to retrieve objects"""
    cities = session.query(City, State).\
        join(State, City.state_id == State.id).\
        order_by(City.id).all()

    for state, city in cities:
        print(f'{state.name}: ({city.id}) {city.name}')
