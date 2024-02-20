#!/usr/bin/python3
"""
script lists all State objects from database using sqlalchemy
"""


import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

from model_state import State, Base


if __name__ == "__main__":
    username, password, db_name = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    """query states and filter state.id = 2"""
    state_object = session.query(State).filter(State.id == 2).one()
    """rename state"""
    state_object.name = "New Mexico"
    session.commit()
