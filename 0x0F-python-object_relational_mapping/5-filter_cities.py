#!/usr/bin/python3
""" Script takes in a state as an argument and lists all cities of state """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor1= db.cursor()
    cursor1.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = cursor1.fetchall()
    temp_p = list(row_data[0] for row_data in rows)
    print(*temp_p, sep=", ")
    cursor1.close()
    db.close()
