#!/usr/bin/python3
"""
script lists all State objects from database using sqlalchemy
"""


import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

from model_state import State, Base


if __name__ == "__main__":
    username, password, db_name, search_term = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    state = session.query(State).\
        filter(State.name == search_term).all()

    if state:
        for each_state in state:
            print(f'{each_state.id}')
    else:
        print('Nothing')
