#!/usr/bin/env python3

# Kiểu số
age = 22
height = 1.75

# Kiểu chuỗi
name = "Minh"

# Kiểu boolean
is_student = True

# In ra
print("Tên:", name)
print("Tuổi:", age)
print("Chiều cao:", height)
print("Sinh viên?:", is_student)

friends = ["An", "Bình", "Chi"]

for f in friends:
    print("Xin chào", f)


def greet(name):
    return f"Hello, {name}!"


print(greet("Minh"))
print(greet("Python"))