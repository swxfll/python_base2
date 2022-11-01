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
# 执行sql
#cursor.execute("create table test_pymysql(id int);")

# 插入数据
cursor.execute("insert into test_pymysql values(5),(6)")
#conn.commit()

cursor.execute("select * from test_pymysql;")
# 遍历数据
results = cursor.fetchall()
for i in results:
    print(i)

# 关闭连接
conn.close()