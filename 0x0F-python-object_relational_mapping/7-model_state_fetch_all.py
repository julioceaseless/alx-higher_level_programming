#!/usr/bin/python3
"""
script lists all State objects from database using sqlalchemy
"""


import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

from model_state import State, Base


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    states = session.query(State).all()
    for state in states:
        print(f'{state.id}: {state.name}')
