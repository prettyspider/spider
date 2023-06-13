# 引用类
import sys
sys.path.append('../db')
from db import db

import lianjie

dbbase = lianjie.dbbase()
# 建立实例
db = db('rooms')
database, cursor = db.discriminant()
def db_insert(sql):
    cursor.execute(sql)
    cursor.commit()

