#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python3 script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2],port = 3306, db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
