#!/usr/bin/env python3

# list = []
# list_clone = []

# for i in range(1, 21):
#     list.append(i)
# print(list)

# for j in list:
#     if j % 2 != 0:
#         list.remove(j)
# print(list)


# list = { "banA" : 1, "banB" : 2, "banC" : 3 }
# print(list)

# list["banD"] = 4
# print(list["banA"])

# list = ["An", "Binh", "Chi"]
# scores = { "An" : 10, "Binh" : 7, "Chi" : 9 }

# for i in scores:
#     if scores[i] >= 8:
#         print(i)

# students = ["An", "Binh", "Chi"]
# scores = {"An": 10, "Binh": 7, "Chi": 9}

# for i in scores.items():
#     print(i)

# num = list(range(1, 21))

# def is_even(num):
#     return num % 2 == 0
    
# even_nums = list(filter(is_even, num))
# print(even_nums)
# -----------------------------------------

# class Student:
#     def __init__(self, name: str, age: int, score: float):
#         self.name = name
#         self.age = age
#         self.score = score
        
#     def grade(self) -> str:
#         if self.score >= 8:
#             return "Gioi"
#         elif self.score >= 6.5:
#             return "Kha"
#         elif self.score >= 5:
#             return "Trung Binh"
#         else:
#             return "Yeu"

# student = Student("An", 20, 9)
# student2 = Student("Binh", 21, 6)
# student3 = Student("Chi", 19, 4)

# print(student.name, student.grade())
# print(student2.name, student2.grade())
# print(student3.name, student3.grade())
    
PhoneBook = {"An": "0123456789", "Binh": "0987654321", "Chi": "0912345678"}

def add(name:str, phone:str):
    PhoneBook[name] = phone
    print("Da them", name)

def get(name:str):
    if name in PhoneBook:
        print(name, ":", PhoneBook[name])
    else:
        print("Khong tim thay", name)

def remove(name:str):
    if name in PhoneBook:
        del PhoneBook[name]
        print("Da xoa", name)
    else:
        print("Khong tim thay", name)

def list_all():
    for name, phone in PhoneBook.items():
        print(name, ":", phone)
        
list_all()
add("Duc", "123")
add("Ech", "456")
add("Fong", "789")
get("An")
remove("Chi")
list_all()
