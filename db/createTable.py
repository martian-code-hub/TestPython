import pymysql
#打开数据库
db = pymysql.connect('localhost','root','123456','openfire')

#使用cursor()方法执行SQL查询
cursor = db.cursor()

cursor.execute('DROP TABLE IF EXISTS PYTHON')

sql = 'CREATE TABLE PYTHON (UNAME varchar(20) NOT NULL, AGE INT, SEX varchar(2))'

cursor.execute(sql)



db.close()