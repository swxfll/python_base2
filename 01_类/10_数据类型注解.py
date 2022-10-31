"""
演示变量的类型注解
"""
import json
import random

# 基础数据类型注解
var_1: int = 10
var_2: str = "swk"
var_3: bool = True


# 类对象类型注解
class Student:
    pass


stu: Student = Student()

# 基础容器类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {"name": "test"}

# 容器类型详细注解
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, str, bool] = (1, "test", True)
my_dict: dict[str, int] = {"name": 123}

# 注释中进行类型注释
var_1 = random.randint(1, 10)  # type: int
var_2 = json.loads('{"name": "swk"}')  # type: dict[str, str]


def func():
    return 10


var_3 = func()  # type: int

# 类型注解仅仅是提示性的，不是决定性的