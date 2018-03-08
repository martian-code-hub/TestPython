import pymysql
#打开数据库
db = pymysql.connect('localhost','root','123456','openfire',use_unicode=True, charset="utf8")

#使用cursor()方法执行SQL查询
cursor = db.cursor()

sql = "INSERT INTO PYTHON(UNAME,AGE,SEX) VALUES('AWIRNGON',123,'女')"

# db.set_character_set('utf8')
# cursor.execute('SET NAMES utf8;')
# cursor.execute('SET CHARACTER SET utf8;')
# cursor.execute('SET character_set_connection=utf8;')

try:
   cursor.execute(sql)

   db.commit()
except Exception as e:
    print('Exception : ',e)
    db.rollback()

db.close()