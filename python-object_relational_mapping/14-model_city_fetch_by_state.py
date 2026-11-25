#!/usr/bin/python3
"""Print each city and its state's name."""
import sys

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session

from model_state import Base, State
from model_city import City


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
        cities = session.query(City, State.name).join(State)
        for city, state_name in cities.order_by(City.id):
            print("{}: ({}) {}".format(state_name, city.id, city.name))
