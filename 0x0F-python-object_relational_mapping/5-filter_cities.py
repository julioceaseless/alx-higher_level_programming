#!/usr/bin/python3
"""
MySQL query to list all cities and their states
from the database hbtn_0e_4_usa. Uses JOIN clause
"""


import sys
import MySQLdb


def print_tuple(tuple_of_tuples):
    if tuple_of_tuples:
        my_list = []
        for each_tuple in tuple_of_tuples:
            my_list.append(each_tuple[0])
        size = len(my_list)
        for i in range(size - 1):
            print("{}, ".format(my_list[i]), end="")
        print(my_list[size - 1])
    else:
        print()


if __name__ == "__main__":
    """Execute code only when called directly"""
    username, password, db_name, state_name = sys.argv[1:]

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password,
                           db=db_name, charset="utf8")
    cur = conn.cursor()
    query = "SELECT cities.name\
            FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s\
            ORDER BY cities.id ASC"
    cur.execute(query, (state_name,))
    query_rows = cur.fetchall()
    print_tuple(query_rows)
    cur.close()
    conn.close()
