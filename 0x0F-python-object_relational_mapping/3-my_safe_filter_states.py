#!/usr/bin/python3
""" Script SQL Injection in the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor1 = db.cursor()
    matching = sys.argv[4]
    cursor1.execute("SELECT * FROM states WHERE name LIKE %s", (matching, ))
    rows = cursor1.fetchall()
    for row_data in rows:
        print(row_data)
    cursor1.close()
    db.close()
