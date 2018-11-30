import pymysql

db = pymysql.connect(host='localhost',
                             user='root',
                             password='123123',
                             db='demo',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

cur=db.cursor()
