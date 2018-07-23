#!/usr/bin/python3
import sqlite3
import sys
import os
import csv


def script_path():
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)  #it seems to be quite important
    return path

def csv_writer(fileOut, dataRows):
    csvDir = "CSV_FILES"
    if not os.path.exists(csvDir):
        os.makedirs(csvDir)
    path = os.path.join(PATH, csvDir)
    path = os.path.join(path, fileOut)
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        for row in dataRows:
            writer.writerow(row)
        print("--< data written to: {}".format(fileOut))
    return True

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
    data = {}
    for table in tables:
        c.execute("SELECT * FROM %s" % table)
        data[table[0]] = c.fetchall()      #store db data in dictio
    return tables, data

def main(args):
    args = ["some.db", "-pt", "-s"]
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
        print("     -pt      print tables to console")
        print("     -pd      print data to console")
        print("     -s      save data in csv files")
        return False

    tables, data = read_db(file)
    if "-pt" in args:
        print(tables)
    if "-pd" in args:
        print(data)
    if "-s" in args:
        for key, row in data.items():
            csv_writer(key + ".csv", row)
    return True


if __name__ == "__main__":
    global PATH; PATH = script_path()
    main(sys.argv[1:])
