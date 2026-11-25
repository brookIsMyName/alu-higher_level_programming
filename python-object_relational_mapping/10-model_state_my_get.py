#!/usr/bin/python3
"""Print the ID of the state with the given name."""
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
        state = session.query(State).filter_by(name=sys.argv[4]).first()
        print("Not found" if state is None else state.id)
