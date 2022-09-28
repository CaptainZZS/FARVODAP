# coding:utf-8
# author: zay
# 连接数据库

import pandas as pd
import pymysql

# 连接数据库
db = pymysql.connect(
    host="localhost",
    database="django",
    user="root",
    password="111",
    port=3306,
    charset='gbk'
)

# sql语句
sqlcmd1 = "select count(*) from data"


# 利用pandas 模块导入mysql数据
a = pd.read_sql(sqlcmd1, db)
print(a)

# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL 删除语句
sqlcmd2 = "DELETE FROM data WHERE  `招聘岗位` IS NULL"
try:
   # 执行SQL语句
   cursor.execute(sqlcmd2)
   # 提交修改
   db.commit()
   a = pd.read_sql(sqlcmd1, db)
   print(a)
   print("delete OK")
except:
   # 发生错误时回滚
   db.rollback()
# 关闭连接
