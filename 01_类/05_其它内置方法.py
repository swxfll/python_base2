"""
魔术方法案例
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__魔术方法
    def __str__(self):
        return f"Student类对象, name:{self.name}, age:{self.name}"

    # __lt__ 魔术方法(小于,大于符号比较)
    def __lt__(self, other):
        return self.age < other.age

    # __le__ 魔术方法 (小于等于,大于等于符号比较)
    def __le__(self, other):
        return self.age <= other.age

    # __eq__ 魔术方法 (==符号比较)
    def __eq__(self, other):
        return  self.age == other.age


stu = Student("孙悟空", 500)
stu2 = Student("猪八戒", 200)

# __str__ 魔术方法
print(stu)  # Student类对象, name:孙悟空, age:孙悟空

# __lt__ 魔术方法(小于,大于符号比较)
print(stu > stu2)  # True
print(stu < stu2)  # False

# __le__ 魔术方法 (小于等于,大于等于符号比较)
print(stu >= stu2)  # True
print(stu <= stu2)  # False

#  __eq__ 魔术方法 (==符号比较)
print(stu == stu2)  # False
