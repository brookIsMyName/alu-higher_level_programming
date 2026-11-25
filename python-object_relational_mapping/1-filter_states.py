#!/usr/bin/python3
"""List states whose names start with uppercase N."""
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
            "WHERE CAST(name AS BINARY) LIKE 'N%' ORDER BY id ASC"
        )
        for row in cursor.fetchall():
            print(row)
