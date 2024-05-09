import sqlite3

def check_table_exists(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
    result = cursor.fetchone()
    return result is not None

# connect to the database
conn = sqlite3.connect('library.db')

# check if the 'books' table exists
if check_table_exists(conn, 'books'):
    print('The "books" table exists.')
else:
    print('The "books" table does not exist.')

# close the connection
conn.close()