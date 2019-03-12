import sqlite3

# This script will drop and create tables
# Be warned

sqlite_file = './rover_db.sqlite'

conn = sqlite3.connect(sqlite_file)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS rovers")
cur.execute("DROP TABLE IF EXISTS cameras")
cur.execute("DROP TABLE IF EXISTS photos")

cur.execute("CREATE TABLE rovers (id INTEGER PRIMARY KEY, name TEXT, max_sols INTEGER, max_date INTEGER, max_photos INTEGER)")

cur.execute("CREATE TABLE cameras(id INTEGER PRIMARY KEY, rover_id INTEGER, abbreviation TEXT, name TEXT, FOREIGN KEY(rover_id) REFERENCES rovers(id))")

cur.execute("CREATE TABLE photos (id INTEGER PRIMARY KEY, rover_id INTEGER, camera_id INTEGER, sol INTEGER, date INTEGER, url TEXT, FOREIGN KEY(rover_id) REFERENCES rovers(id), FOREIGN KEY (camera_id) REFERENCES cameras(id))")

conn.commit()

# TODO Maybe load manifest data on the first run?