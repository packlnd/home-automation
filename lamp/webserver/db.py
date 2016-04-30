import sqlite3

db = sqlite3.connect('db.db')
cur = db.cursor()
cur.execute("CREATE TABLE Lamp(Id INT, On TEXT, Off TEXT, Duration INT)")

def write_to_db(on, off, duration):
    cur = db.cursor()
    cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")

def read_from_db():
    cur = db.cursor()
    cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
