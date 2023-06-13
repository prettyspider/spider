import db
import pymysql
def dbbase():
    # 创建实例
    try:
        db1 = db.db()
        database1, cursor1 = db1.discriminant()
        sql = 'create database rooms'
        cursor1.execute(sql)
    except pymysql.err.ProgrammingError:
        print('database exists')

    try:
        db2 = db.db('rooms')
        database2, cursor2 = db2.discriminant()
        print(database1, database2)
        # 创建表lianjia
        """"
        房子名 title  varchar
        价格 price int
        图片img varchar
        地址 address varchar
        面积area int 单位是平方米
        方位direction varchar
        楼高 buildingheight int 单位是楼
        优势advantage varchar
        住宿条件 housecondition varchar
        """
        sql_create = "create table lianjia(" \
                     "id int primary key auto_increment," \
                     "title  varchar(255)," \
                     "price int," \
                     "img VARCHAR(255)," \
                     "address varchar(255)," \
                     "areas varchar(255)," \
                     "direction varchar(255)," \
                     "buildingheight int ," \
                     "conditions varchar(255)" \
                     ")"
        cursor2.execute(sql_create)
    except pymysql.err.OperationalError:
        print("table exists")
