#!/usr/bin/python3
"""List every city alongside its state name."""
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
            "SELECT cities.id, cities.name, states.name "
            "FROM cities JOIN states ON cities.state_id = states.id "
            "ORDER BY cities.id ASC"
        )
        for row in cursor.fetchall():
            print(row)
