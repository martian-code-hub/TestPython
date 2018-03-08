import pymysql
#打开数据库
db = pymysql.connect('localhost','root','123456','openfire',use_unicode=True, charset="utf8")

#使用cursor()方法执行SQL查询
cursor = db.cursor()

sql = "DELETE FROM PYTHON  WHERE UNAME = 'AWIRNGON'"

try:
   cursor.execute(sql)

   db.commit()
except Exception as e:
    print('Exception : ',e)
    db.rollback()

db.close()