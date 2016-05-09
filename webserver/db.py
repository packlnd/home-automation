import sqlite3

db = sqlite3.connect('db.db')

def write_status_to_db(on, off, duration):
    cur = db.cursor()
    cur.execute("INSERT INTO  VALUES(1,'Audi',52642)")

def write_alarm_to_db(alarm):
    cur = db.cursor()

def read_from_db():
    cur = db.cursor()
    cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
