import sqlite3

conn = sqlite3.connect("data/Ruby.db")
conn.row_factory = sqlite3.Row
cur = conn.cursor()

def create_tables():
    cur.execute("""CREATE TABLE IF NOT EXISTS servers(id TEXT, type TEXT, value TEXT)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS blacklist(id TEXT, name TEXT, discrim TEXT, reason TEXT)""")

def insert_data_entry(id, type, value):
    cur.execute("""INSERT INTO servers(id, type, value) VALUES (?, ?, ?)""", (id, type, value))
    conn.commit()

def read_data_entry(id, type):
    cur.execute("""SELECT value FROM servers WHERE id=(?) AND type=(?)""", (id, type))
    val = None
    try:
        val = cur.fetchone()[0]
    except:
        if type == "mod-role":
            insert_data_entry(id, type, "Mods")
            val = "Mods"
        elif type == "nsfw-channel":
            insert_data_entry(id, type, "nsfw")
            val = "nsfw"
        elif type == "mute-role":
            insert_data_entry(id, type, "Muted")
            val = "Muted"
        elif type == "join-message":
            insert_data_entry(id, type, None)
            val = None
        elif type == "leave-message":
            insert_data_entry(id, type, None)
            val = None
        elif type == "join-leave-channel":
            insert_data_entry(id, type, None)
            val = None
        elif type == "join-role":
            insert_data_entry(id, type, None)
            val = None
    return val

def update_data_entry(id, type, value):
    exists = read_data_entry(id, type)
    cur.execute("""UPDATE servers SET value=(?) WHERE id=(?) AND type=(?)""", (value, id, type))
    conn.commit()

def delete_data_entry(id, type):
    cur.execute("""DELETE FROM servers WHERE id=(?) AND type=(?)""", (id, type))
    conn.commit()

def blacklistuser(id, name, discrim, reason):
    cur.execute("""INSERT INTO blacklist(id, name, discrim, reason) VALUES (?, ?, ?, ?)""", (id, name, discrim, reason))
    conn.commit()

def unblacklistuser(id):
    cur.execute("""DELETE FROM blacklist WHERE id=""" + id)
    conn.commit()

def getblacklistentry(id):
    cur.execute("""SELECT id FROM blacklist WHERE id=""" + id)
    id = None
    name = None
    discrim = None
    reason = None
    try:
        id = cur.fetchone()[0]
    except:
        return None
    cur.execute("""SELECT name FROM blacklist WHERE id=""" + id)
    name = cur.fetchone()[0]
    cur.execute("""SELECT discrim FROM blacklist WHERE id=""" + id)
    discrim = cur.fetchone()[0]
    cur.execute("""SELECT reason FROM blacklist WHERE id=""" + id)
    reason = cur.fetchone()[0]
    blacklistentry = {"id":id, "name":name, "discrim":discrim, "reason":reason}
    return blacklistentry

def getblacklist():
    cur.execute("""SELECT id, name, discrim, reason FROM blacklist""")
    entries = []
    rows = cur.fetchall()
    for row in rows:
        entry = "ID: \"" + row["id"] + "\" Name: \"" + row["name"]  + "\" Discrim: " + row["discrim"] + " Reason: \"" + row["reason"] + "\""
        entries.append(entry)
    return entries

create_tables()
