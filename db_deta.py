import deta
from datetime import datetime

deta_key = "b0h8zhplclp_qDRmec9egwnXokAT85zdVgoPo2koyFVk"

# Connect to the database
deta = deta.Deta(deta_key)
db = deta.Base("guestbook")

# Add a new entry to the database
def add_entry(name, message):
    # Add a timestamp when inserting a new entry
    entry = {
        "name": name,
        "message": message,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    db.put(entry)

# Get all entries from the database
def get_entries():
    entries = db.fetch().items
    return entries

# Delete specific entries from the database
def delete_entries(ids):
    for id in ids:
        db.delete(id)

# Close the database connection when done
def close():
    pass  # No need to close connection for Deta database