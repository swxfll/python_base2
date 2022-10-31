class Student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None

# 创建一个对象
stu_1 = Student()

# 对象属性赋值
stu_1.name = "孙悟空"
stu_1.gender = "男"
stu_1.nationality = "中国"
stu_1.native_place = "花果山"
stu_1.age = 500

# 输出
print(type(stu_1))  # <class '__main__.Student'>
print(stu_1.name)  # 孙悟空