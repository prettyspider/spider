import pymysql as sql
class db:
    def __init__(self,database=''):
        self.database=database
        self.db=''
        self.cursor=''
    # 判别数据库是否写在配置文件中
    def discriminant(self):
        if self.database=='':
            return self.get_no_database()
        else:
            return self.get_database()
    # 不存在database参数
    def get_no_database(self):
        self.db = sql.connect(
            host="localhost",  # 主机ip
            user="root",  # 数据库用户
            password="12345678",  # 用户对应的密码
            # 不屑对应的数据库名，未后期建立数据库流空间
            database=self.database,
            # database="momandboby",  # 对应的数据库
            port=3306,  # 数据库端口，默认3306
            charset='utf8'  # 数据库编码
        )
        self.cursor=self.db.cursor()
        return [self.db,self.cursor]
    # 存在的数据库
    def get_database(self):
        self.db = sql.connect(
            host="localhost",  # 主机ip
            user="root",  # 数据库用户
            password="12345678",  # 用户对应的密码
            # 不屑对应的数据库名，未后期建立数据库流空间
            database=self.database,
            # database="momandboby",  # 对应的数据库
            port=3306,  # 数据库端口，默认3306
            charset='utf8'  # 数据库编码
        )
        self.cursor=self.db.cursor()
        return [self.db,self.cursor]




