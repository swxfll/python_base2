

from pymysql import Connection

# 新建Mysql数据库的连接
conn = Connection(
    host="192.168.111.223",
    port=3306,
    user="ll",
    password="123abc",
    autocommit=True     # 无需手动提交
)

print(conn.get_server_info())

# 获取游标对象
cursor = conn.cursor()

# 选择数据库
conn.select_db("test")

cursor.execute("""
CREATE TABLE student(
	id INT,
    name VARCHAR(20),
    age INT,
    gender VARCHAR(10)
);
""")

cursor.close()