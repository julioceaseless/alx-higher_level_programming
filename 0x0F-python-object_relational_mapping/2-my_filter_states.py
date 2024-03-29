#!/usr/bin/python3
"""
Query MYSQL database via python
"""


import sys
import MySQLdb

if __name__ == "__main__":
    """query database with MYSQL"""
    username, password, db_name, state_name = sys.argv[1:]

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password,
                           db=db_name, charset="utf8")
    cur = conn.cursor()
    query = "SELECT * FROM states\
            WHERE name = '{}'\
            ORDER BY id ASC".format(state_name)
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
