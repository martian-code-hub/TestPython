import pymysql
#打开数据库
db = pymysql.connect('localhost','root','123456','openfire',use_unicode=True, charset="utf8")

#使用cursor()方法执行SQL查询
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM PYTHON WHERE AGE > '%d'" % (18)

try:
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        uName = row[0]
        age = row[1]
        sex = row[2]

        print('uName = %s , age = %s , sex = %s' % (uName,age,sex))
except Exception as e:
    print('Exception : ' % (e))
db.close()