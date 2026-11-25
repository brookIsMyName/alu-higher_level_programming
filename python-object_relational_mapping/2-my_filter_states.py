#!/usr/bin/python3
"""Find states whose names match the argument."""
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
        # A hexadecimal SQL literal holds the UTF-8 bytes of any input.
        state_hex = sys.argv[4].encode("utf-8").hex()
        cursor.execute(
            "SELECT * FROM states "
            "WHERE CAST(CONVERT(name USING utf8mb4) AS BINARY) = X'{}' "
            "ORDER BY id ASC".format(state_hex)
        )
        for row in cursor.fetchall():
            print(row)
