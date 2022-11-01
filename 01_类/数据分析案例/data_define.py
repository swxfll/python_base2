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

    def to_dict(self):
        return {
            'date': str(self.date),
            'order_id': self.order_id,
            'money': int(self.money),
            'province': self.province
        }

    """
    添加 __iter__ 和 __next__ 方法让对象支持迭代。
    从而支持dict(对象名)方法
    """
    def __iter__(self):
        return next(self)

    def __next__(self):
        yield 'date', str(self.date)
        yield 'order_id', self.order_id
        yield 'money', int(self.money)
        yield 'province', self.province


if __name__ == '__main__':
    record = Record('2022-01-01', 'asdasdad', 12123, '广东省')
    print(record)
    print(record.to_dict())
    print(dict(record))

