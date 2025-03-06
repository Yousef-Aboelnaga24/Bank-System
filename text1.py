# class Person:
#     def __init__(self, name, age, adress, phone):


#         self.name = name
#         self.age = age
#         self.adress = adress
#         self.phone = phone

#         self.count = 0
#     def counter(self):
#        self.count += 1

#     def display_info(self):
#         print(f'Name: {self.name} Age: {self.age} Address: {self.adress} Phone: {self.phone}')


# person_1 = Person('yosef', 17, 'giza', '01234567890')
# person_1.name = 'ahmed'

# person_1.display_info()

# ==================================================================

# class Student:

#     school_name = 'WE Applied Technology Schools'
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

#     def display_info(self):
#         print(f'Name: {self.name}\nGrades: {self.grade}\nSchool: {Student.school_name}')

# student_1 = Student('yousef', '2nd')
# student_1.display_info()

# ==================================================================

# class Book:
#     def __init__(self, title, auther):
#         self.title = title
#         self.auther = auther
#         self.borrowed = False
    
#     def borrowed_book(self):
#         if not self.borrowed:
#             self.borrowed = True
#             print(f'{self.title} by {self.auther} has been borrowed')
#         else:
#             print(f'{self.title} is currently not available')

#     def return_book(self):
#         if self.borrowed:
#             self.borrowed = False
#             print(f'{self.title} has been returned')
#         else:
#             self.borrowed = True
#             print(f'{self.title} was borrowed')

# book_1 = Book('Python Programming', 'ahmed ali')

# book_1.borrowed_book()
# book_1.return_book()