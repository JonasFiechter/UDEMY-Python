import sqlite3


class AgendaDB:
    def __init__(self, file):
        self.conn = sqlite3.connect(file)
        self.cursor = self.conn.cursor()

    def insert(self, name, tel):
        consult = 'INSERT OR IGNORE INTO agenda (name, tel) VALUES (?, ?)'
        self.cursor.execute(consult, (name, tel))
        self.conn.commit()

    def edit(self, name, tel, id):
        consult = 'UPDATE agenda SET name=?, tel=? WHERE id=?'
        self.cursor.execute(consult, (name, tel, id))
        self.conn.commit()

    def delete(self, id):
        consult = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consult, (id,))
        self.conn.commit()

    def list(self):
        self.cursor.execute('SELECT * FROM agenda')
        for line in self.cursor.fetchall():
            print(line)

    def search(self, value):
        self.cursor.execute('SELECT * FROM agenda WHERE name LIKE ?', (f'%{value}%',))
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    agenda.insert('Luix', '12345')
    agenda.search('Lu')
