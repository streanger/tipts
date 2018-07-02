#!/usr/bin/python3
import sqlite3
import pandas as pd
import sys, os

def create_db(file):
    #example db
    conn = sqlite3.connect(file)
    c = conn.cursor()
    # Create table
    c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
    c.execute('''CREATE TABLE others (date text, trans text, things text, qty real, cost real)''')
    # Insert a row of data
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    c.execute("INSERT INTO others VALUES ('2006-01-05','BUY','RHAT',88,21.14)")
    # Save (commit) the changes
    conn.commit()
    conn.close()

def read_db(file):
    conn = sqlite3.connect(file)
    c = conn.cursor()
    try:
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    except sqlite3.DatabaseError as err:
        print("file is not a database...")
        return False
    tables = c.fetchall()
    print("tables:", tables)

    for table in tables:
        c.execute("SELECT * FROM %s" % table)
        print(table, ":", c.fetchall())
    return True

def main(args):
    file = ""
    if args:
        file = args[0]
        if not file.endswith(".db"):
            print("wrong file type")
            sys.exit()
        if not os.path.isfile(file):
            print("no such file in current dir")
            sys.exit()
    else:
        print("usage:")
        print("     <script> <some.db>")
        print("     script will read entire db into terminal")
        sys.exit()
    #create_db(file)
    read_db(file)

if __name__ == "__main__":
    main(sys.argv[1:])
