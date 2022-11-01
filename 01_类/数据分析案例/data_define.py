"""
实体类
"""


class Record:
    def __init__(self, date, order_id, money, province):
        self.date = date  # 订单日期
        self.order_id = order_id  # 订单ID
        self.money = money  # 订单金额
        self.province = province  # 销售省份

    def __str__(self):
        return f"订单日期: {self.date}, 订单ID: {self.order_id}, 订单金额: {self.money}, 销售省份: {self.province}"
