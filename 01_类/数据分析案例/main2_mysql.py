"""
面向对象, 数据分析案例
实现步骤:
1. 设计一个类, 可以完成数据的封装
2. 设计一个抽象类, 定义文件读取的相关功能
3. 读取文件,生成数据对象
4. 将数据写入mysql
5. 将数据从mysql读出, 写入文件
"""

from file_define import FileReader, TextFileReader, JsonFileReader
from data_define import Record
from pymysql import Connection

text_file_reader = TextFileReader("2011年1月销售数据.txt")
text_file_date: list[Record] = text_file_reader.read_data()

json_file_reader = JsonFileReader("2011年2月销售数据JSON.txt")
json_file_data: list[Record] = json_file_reader.read_data()

# 将2个月份的数据合并为1个list来存储
all_data: list[Record] = text_file_date + json_file_data

# 构建Mysql对象
conn = Connection(
    host="192.168.111.223",
    port=3306,
    user="ll",
    password="123abc",
    autocommit=True,
)

# 获取游标对象
cursor = conn.cursor()
# 删除和创建数据库
cursor.execute("DROP DATABASE IF EXISTS py_sql")
cursor.execute("create database py_sql charset='utf8mb4'")
# 选择数据库
conn.select_db("py_sql")
# 删除和创建表
cursor.execute("DROP TABLE IF EXISTS orders;")
cursor.execute("create table orders(date Date, order_id varchar(255), money decimal(10, 2), province varchar(10))")

# 插入数据
for item in all_data:
    sql = f"insert into orders values('{item.date}', '{item.order_id}', '{item.money}', '{item.province}')"

    # 执行sql
    cursor.execute(sql)


# 查询并写入文件
cursor.execute("SELECT * FROM orders limit 1000")
str_list = []
for item in cursor.fetchall():
    record = Record(item[0], item[1], item[2], item[3])
    str_list.append(str(dict(record)) + "\n")

f = open("text.txt", "w", encoding="UTF-8")
for item in str_list:
    f.write(item)
f.close()

# 关闭数据库连接
conn.close()