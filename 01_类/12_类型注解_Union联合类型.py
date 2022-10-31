# 使用Union类型, 必须先导包
from typing import Union

my_list: list[Union[int, str]] = [1, 2, "孙悟空", "猪八戒"]

def func(data: Union[int, str]) -> Union[int, str]:
    pass