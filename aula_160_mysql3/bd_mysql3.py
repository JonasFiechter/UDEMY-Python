import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clients ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'name TEXT,'
               'weight REAL'
               ')')

cursor.execute('INSERT INTO clients (name, weight) VALUES (:name, :weight)',
               {'name': 'John', 'weight': 244
               })

cursor.execute('INSERT INTO clients VALUES (:id, :name, :weight)',
               {'id': None, 'name': 'Marco', 'weight': 234
               })

connection.commit()

cursor.execute('UPDATE clients SET name=:name WHERE id=:id',
               {'name': 'teste', 'id': 2})

cursor.execute('DELETE FROM clients WHERE id<5')

cursor.execute('SELECT * FROM clients')

for line in cursor.fetchall():
    print(line)

cursor.close()
connection.close()