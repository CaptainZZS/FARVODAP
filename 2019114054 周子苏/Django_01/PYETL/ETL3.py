import pandas as pd
import pymysql


db = pymysql.connect(
        host="localhost",
        database="django",
        user="root",
        password="111",
        port=3306,
        charset='gbk'
    )

def find_data(x,y,z,k):
    sql1 = "SELECT * FROM DATA WHERE 城市 = '%s' AND 公司类型 = '%s' AND 学历 = '%s' AND 工作经验 = '%s'" % (x,y,z,k)
    a = pd.read_sql(sql1, db)
    list1 = a.values.tolist()
    return list1
