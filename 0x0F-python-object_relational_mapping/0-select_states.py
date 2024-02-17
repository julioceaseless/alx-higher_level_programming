#!/usr/bin/env python3
import sys
import MySQLdb

mysql_user = sys.argv[1]
mysql_passwd = sys.argv[2]
mysql_db = sys.argv[3]

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=mysql_user, passwd=mysql_passwd,
                           db=mysql_db, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
