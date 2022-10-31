"""
开学了有一批学生信息需要录入系统，请设计一个类，记录学生的：
姓名、年龄、地址，这3类信息
请实现：
通过for循环，配合input输入语句，并使用构造方法，完成学生信息的键盘录入
输入完成后，使用print语句，完成信息的输出
"""

class Student:
    name = None
    age = None
    address = None

    def __init__(self, uname, uage, uaddress):
        self.name = uname
        self.age = uage
        self.address = uaddress

    def stu_info(self):
        return f"学生姓名: {self.name}, 年龄: {self.age}, 地址: {self.address}"


# 定义列表,存储10个学生的信息
user_list = []

for i in range(1, 3):
    print(f"当前录入第{i}位学生信息, 总共需录入10位学生信息")

    uname = input("请输入姓名")
    uage = input("请输入年龄")
    uaddr = input("请输入地址")

    stu = Student(uname, uage, uaddr)

    user_list.append(stu)

    print(f"学生{i}信息录入完成, 信息为: {stu.stu_info()}")


