import sqlite3

db_locale = 'students.db'

connie = sqlite3.connect(db_locale)
c = connie.cursor()

c.execute("""
CREATE TABLE contact_details
(id INTEGER PRIMARY KEY AUTOINCREMENT,
firstname TEXT,
surname TEXT,
street_address TEXT,
suburb TEXT
)
""")

connie.commit()
connie.close()
