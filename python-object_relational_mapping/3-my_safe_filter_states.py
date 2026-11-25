#!/usr/bin/python3
"""Find states by name using a bound MySQLdb parameter."""
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
            "SELECT * FROM states "
            "WHERE CAST(CONVERT(name USING utf8mb4) AS BINARY) = "
            "CAST(%s AS BINARY) ORDER BY id ASC",
            (sys.argv[4],),
        )
        for row in cursor.fetchall():
            print(row)
