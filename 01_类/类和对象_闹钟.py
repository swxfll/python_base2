"""
演示类和对象的关系
"""


# 设计一个闹钟类
class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)


# 创建2个闹钟对象
clock1 = Clock()
clock1.ring()

clock2 = Clock()
clock2.ring()
