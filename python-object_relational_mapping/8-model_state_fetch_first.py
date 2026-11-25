#!/usr/bin/python3
"""Print the state with the smallest ID."""
import sys

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session

from model_state import Base, State


if __name__ == "__main__":
    url = URL.create(
        "mysql+mysqldb",
        username=sys.argv[1],
        password=sys.argv[2],
        host="localhost",
        port=3306,
        database=sys.argv[3],
        query={"charset": "utf8mb4"},
    )
    engine = create_engine(url, pool_pre_ping=True)
    with Session(engine) as session:
        state = session.query(State).order_by(State.id).first()
        if state is None:
            print("Nothing")
        else:
            print("{}: {}".format(state.id, state.name))
