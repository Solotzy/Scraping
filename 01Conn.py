import pymysql

# 连接对象
conn = pymysql.connect(host='192.168.1.190', unix_socket='/tem/mysql.sock',user='root',passwd=None,db='mysql')

# 光标对象
cur = conn.cursor()
cur.execute("USE scraping")

cur.execute("SELECT * FROM pages WHERE id=1")
print(cur.fetchone())
cur.close()
conn.close()

