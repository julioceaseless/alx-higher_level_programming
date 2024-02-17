#!/usr/bin/python3
import sys
import MySQLdb
"""Query MYSQL database via python"""


if __name__ == "__main__":
    username, password, name = sys.argv[1:]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password,
                           db=name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
