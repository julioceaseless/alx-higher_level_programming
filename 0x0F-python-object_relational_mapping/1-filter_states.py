#!/usr/bin/python3
"""
list all states with a name starting with N (upper N)
from the database
"""


import sys
import MySQLdb

def main(username, password, db_name):
    """Queries the database

    Args:
        username: database username
        password: user's password
        db_name: database name
    """

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password,
                           db=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    """don't run when imported"""

    main(sys.argv[1], sys.argv[2], sys.argv[3])
