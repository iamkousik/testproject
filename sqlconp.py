import mysql.connector

try:
    f = mysql.connector.connect(user='kousik', password='712407',
                            host='localhost', database='kousik',)
    print('connected....')
    f.close()
except Exception as e:
    print(e)
finally:
    print('Bay!')