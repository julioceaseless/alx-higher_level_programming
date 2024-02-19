#!/usr/bin/python3
"""
Query MYSQL database safely to avoid injections. This is done
by passing user input as parameter to the execute() function
"""


import sys
import MySQLdb

if __name__ == "__main__":
    """Execute code only if called directly"""
    username, password, db_name, state_name = sys.argv[1:]

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password,
                           db=db_name, charset="utf8")
    cur = conn.cursor()
    query = "SELECT * FROM states\
            WHERE name = %s\
            ORDER BY id ASC"
    cur.execute(query, (state_name,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
