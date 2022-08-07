import sqlite3

db_locale = 'students.db'

connie = sqlite3.connect(db_locale)
c = connie.cursor()

c.execute("""
INSERT INTO contact_details (firstname, surname, street_address, suburb) VALUES
('John1', 'John1', 'Street', 'Espoo'),
('John2', 'Joh2', 'Street', 'Espoo'),
('John3', 'John3', 'Street', 'Espoo')
""")

connie.commit()
connie.close()