import pymysql
#打开数据库
db = pymysql.connect('localhost','root','123456','openfire')

#使用cursor()方法执行SQL查询
cursor = db.cursor()

#使用 excute()犯法执行SQL查询
cursor.execute('SELECT VERSION()')

#使用fetchone()方法获取单条数据
data = cursor.fetchone()

print('Database version : %s ' % data)

#关闭数据库连接
db.close()
