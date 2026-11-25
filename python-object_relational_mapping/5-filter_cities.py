#!/usr/bin/python3
"""List the cities of a state in city ID order."""
from contextlib import closing
import sys

import MySQLdb


if __name__ == "__main__":
    with closing(MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8mb4",
    )) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(
            "SELECT cities.name FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "WHERE CAST(CONVERT(states.name USING utf8mb4) AS BINARY) = "
            "CAST(%s AS BINARY) "
            "ORDER BY cities.id ASC",
            (sys.argv[4],),
        )
        print(", ".join(name for (name,) in cursor.fetchall()))
