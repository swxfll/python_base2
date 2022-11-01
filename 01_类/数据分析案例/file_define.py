import json

from data_define import Record


# 定义一个抽象类,用来做顶层设计, 确定有哪些功能需要实现
class FileReader:

    def read_data(self) -> list[Record]:
        """
        读取文件的数据,
        读到的每一条数据都转为Record对象,
        将它们都封装到list返回
        """
        pass


class TextFileReader(FileReader):

    def __init__(self, path):
        self.path = path  # 定义成员变量,记录文件的路径

    # 复写(实现抽象方法)
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list = []
        for line in f.readlines():
            line = line.strip()     # 去除每一行数据的换行符
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list


class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path  # 定义成员变量,记录文件的路径

    # 复写(实现抽象方法)
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list


if __name__ == '__main__':
    text_file_reader = TextFileReader("2011年1月销售数据.txt")
    list1 = text_file_reader.read_data()
    for item in list1:
        print(item)

    json_file_reader = JsonFileReader("2011年2月销售数据JSON.txt")
    list2 = json_file_reader.read_data()
    for item in list2:
        print(item)