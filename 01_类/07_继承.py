"""
演示面向对象: 继承的基础语法
"""


# 演示单继承
class Phone:
    IMEI = 2
    producer = "SY"

    def call_by_4g(self):
        print("4g通话")


class Phone2022(Phone):
    face_id = "10001"

    def call_by_5g(self):
        print("2022年新增功能: 5g通话")


phone = Phone2022()
print(phone.call_by_4g())
