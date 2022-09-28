# -*- coding: utf-8 -*-# 导入必要模块
import pandas as pd
from sqlalchemy import create_engine
# 初始化数据库连接，使用pymysql模块
db_info = {'user': 'root', 'password': '111', 'host': 'localhost', 'port': 3306, 'database': 'django' }
engine = create_engine('mysql+pymysql://%(user)s:%(password)s@%(host)s:%(port)d/%(database)s?charset=gbk' % db_info, encoding='gbk')
df = pd.read_csv("../data_analysis_job.csv", encoding='gbk')
df.to_sql('datas', engine,if_exists = 'append',index= False)
