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

    """ create a new  Louisiana state"""
    louisiana = State(name='Louisiana')
    session.add(louisiana)
    session.commit()

    """query all states"""
    state = session.query(State).filter(State.name == 'Louisiana').first()
    print(f'{state.id}')
