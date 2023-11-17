#!/usr/bin/python3
"""lists all State objects from the database.
"""

from model_state import Base, State
from sqlalchemy import create_engine, select
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    stmt = select([
        State.id, State.name
        ]).order_by(State.id.asc())

    connection = engine.connect()
    results = connection.execute(stmt).fetchall()

    for res in results:
        print("{}: {}".format(res[0], res[1]))
