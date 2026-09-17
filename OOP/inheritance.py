class Person:

    def __init__(self,name, age):
        self.__name = name
        self.__age = age

    def name(self):
        return self.__name

    def age(self):
        return self.__age

    def displayInfo(self):
        print(f"{self.__name}, {self.__age}")

class Workers(Person):

    def bio(self):
        print(f"Name: {self.name()}, age: {self.age()}")

John = Workers("John", 25)
print(John.name())
John.displayInfo()
John.bio()