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

sqlcmd1 = "select * from data"
a = pd.read_sql(sqlcmd1, db)
list1 = a.values.tolist()
beijing_list = []
shanghai_list = []
guangzhou_list = []
shenzheng_list = []
wuhan_list = []
chongqing_list = []
hangzhou_list = []
suzhou_list = []
tianjing_list = []
nanjing_list = []
changshang_list = []
xiameng_list = []
for i in list1:
        if i[0] == "北京":
            beijing_list.append(i)
        elif i[0] == "上海":
            shanghai_list.append(i)
        elif i[0] == "广州":
            guangzhou_list.append(i)
        elif i[0] == "深圳":
            shenzheng_list.append(i)
        elif i[0] == "武汉":
            wuhan_list.append(i)
        elif i[0] == "重庆":
            chongqing_list.append(i)
        if i[0] == "杭州":
            hangzhou_list.append(i)
        elif i[0] == "苏州":
            suzhou_list.append(i)
        elif i[0] == "天津":
            tianjing_list.append(i)
        elif i[0] == "南京":
            nanjing_list.append(i)
        elif i[0] == "长沙":
            changshang_list.append(i)
        elif i[0] == "厦门":
            xiameng_list.append(i)

def beijing():
        global beijing_list
        return beijing_list
def shanghai():
        global shanghai_list
        return shanghai_list
def guangzhou():
        global guangzhou_list
        return guangzhou_list
def shenzheng():
        global shenzheng_list
        return shenzheng_list
def wuhan():
        global wuhan_list
        return wuhan_list
def chongqing():
        global chongqing_list
        return chongqing_list
def hangzhou():
        global hangzhou_list
        return hangzhou_list
def suzhou():
        global suzhou_list
        return suzhou_list
def tianjing():
        global tianjing_list
        return tianjing_list
def nanjing():
        global nanjing_list
        return nanjing_list
def changshang():
        global changshang_list
        return changshang_list
def xiameng():
        global xiameng_list
        return xiameng_list




