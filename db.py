import sqlite3

# Connect to the database (creates a new file if it doesn't exist)
conn = sqlite3.connect('guestbook.db')

# Create a table for guestbook entries
conn.execute('''CREATE TABLE IF NOT EXISTS entries
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  message TEXT,
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

# Add a new entry to the database
def add_entry(name, message):
    conn.execute("INSERT INTO entries (name, message) VALUES (?, ?)", (name, message))
    conn.commit()

# Get all entries from the database
def get_entries():
    cursor = conn.execute("SELECT id, name, message, created_at FROM entries ORDER BY created_at DESC")
    entries = [{'id': row[0], 'name': row[1], 'message': row[2], 'created_at': row[3]} for row in cursor.fetchall()]
    return entries

# Delete specific entries from the database
def delete_entries(ids):
    conn.executemany("DELETE FROM entries WHERE id = ?", [(id,) for id in ids])
    conn.commit()

# Close the database connection when done
def close():
    conn.close()
