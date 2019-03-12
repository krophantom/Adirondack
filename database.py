import sqlite3

sqlite_file = './rover_db.sqlite'

# Run db setup first!!!

conn = sqlite3.connect()

cur = conn.cursor()

# Do nothing so far

conn.close()
