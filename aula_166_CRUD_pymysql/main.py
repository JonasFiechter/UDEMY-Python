import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def connecting():
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield connection
    finally:
        print('closed')
        connection.close()


with connecting() as conecta:
    with conecta.cursor() as cursor:
        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
              '(%s, %s, %s, %s)'
        cursor.execute(sql, ('Jack', 'Monroe', 112, 220))
        conecta.commit()

with connecting() as conecta:
    with conecta.cursor() as cursor:
        sql = 'DELETE FROM clientes WHERE id = %s'
        cursor.execute(sql, (7,))
        conecta.commit()

with connecting() as conecta:
    with conecta.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes LIMIT 100')
        result = cursor.fetchall()
        for line in result:
            print(line['id'], line['nome'], line['sobrenome'])