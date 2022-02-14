import mysql.connector 


class ConnectToDB:
    def __init__(self):
        self.conn = mysql.connector.connect(host='localhost',
                                            database='db_001',
                                            user='user',
                                            password='jm')
                                            
    def connect(self):
        """ Connect to MySQL database """

        if self.conn.is_connected():
            print('connected to MySQL database')

    def disconnect(self):
        """ Disconnect from MySQL database """

        if self.conn.is_connected():
            print('still connected')
            self.conn.close()
            print('disconnected')
        
        else:
            print('not connected')


if __name__ == '__main__':
    conn_1 = ConnectToDB()
    conn_1.disconnect()