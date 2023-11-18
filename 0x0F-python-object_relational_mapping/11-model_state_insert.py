#!/usr/bin/python3
"""Adds the State object “Louisiana” to the database
"""

from model_state import Base, State
from sqlalchemy import create_engine, select
import sys
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    loisiana = State(name="Louisiana")
    session.add(loisiana)
    session.commit()
    print(loisiana.id)
    session.close()
