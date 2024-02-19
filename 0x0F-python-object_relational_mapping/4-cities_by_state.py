#!/usr/bin/python3
"""
MySQL query to list all cities and their states
from the database hbtn_0e_4_usa. Uses JOIN clause
"""


import sys
import MySQLdb

if __name__ == "__main__":
    """Execute code only when called directly"""
    username, password, db_name = sys.argv[1:]

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password,
                           db=db_name, charset="utf8")
    cur = conn.cursor()
    query = "SELECT cities.id, cities.name, states.name\
            FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC"
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
