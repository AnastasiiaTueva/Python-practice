class Workers:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.salary = salary

    def set_age(self, age):
        if 0 < age < 100:
            self.__age = age
        else:
            print("Error")

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def printWorker(self):
        print(f"name: {self.__name}, age: {self.__age}, salary: {self.salary}")


John = Workers("John", 23, 1000)

John.__name = "Jack"
John.__age = 35
John.salary = 1200

John.printWorker()
