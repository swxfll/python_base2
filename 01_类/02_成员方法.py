"""
演示面向对象,类中的成员方法定义和使用
"""


# 定义一个带有成员方法的类
class Student:
    name = None  # 姓名

    def say_hi(self):
        print(f"大家好, 我是{self.name}")

    def say_hi2(self, msg):
        print(f"大家好, 我是{self.name}, {msg}")


stu = Student()
stu.name = "孙悟空"
stu.say_hi()  # 大家好, 我是孙悟空
stu.say_hi2("金箍棒")  # 大家好, 我是孙悟空, 金箍棒

stu2 = Student()
stu2.name = "猪八戒"
stu2.say_hi()  # 大家好, 我是猪八戒
stu2.say_hi2("九齿钉耙")  # 大家好, 我是猪八戒, 九齿钉耙
