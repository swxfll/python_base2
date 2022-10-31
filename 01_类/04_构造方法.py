class Student:
    name = None
    age = None
    weapon = None

    def __init__(self, name, age, weapon):
        self.name = name
        self.age = age
        self.weapon = weapon
        print("Student类创建了一个类对象")


swk = Student("孙悟空", 500, "如意金箍棒")
