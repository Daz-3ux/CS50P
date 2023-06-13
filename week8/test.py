# A class is like a mold for a type of data 
# where we can invent our own data type and give them a name.
class Student:
    def __init__(self, name, house): # 构造函数
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house

    def __str__(self): # 用于打印对象
        return f"{self.name} from {self.house}"

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, name): # _name 只能通过 name setter 进行设置
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # Getter for house
    @property # 将一个方法转化为类的属性
    def house(self):
        return self._house
    
    # Setter for house
    @house.setter # 属性设置器: 只要设置房屋属性就会调用该函数
    def house(self, house): # _house 只能通过 house setter 进行设置
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house



def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()