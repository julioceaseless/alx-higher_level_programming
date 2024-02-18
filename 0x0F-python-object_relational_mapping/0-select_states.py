#!/usr/bin/python3
"""
Query MYSQL database via python
"""


import sys
import MySQLdb

if __name__ == "__main__":
    """query database with MYSQL"""
    username, password, name = sys.argv[1:]

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password,
                           db=name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
