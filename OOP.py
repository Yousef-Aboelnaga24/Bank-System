class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name

    def display_info(self):
        print(f'Name: {self.name} \nAge: {self.age}')

person_1 = Person('yousef', 17)

person_1.display_info()
person_1.get_name()