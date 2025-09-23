#!/usr/bin/env python3

n = int(input("Enter your number:"))

def check_number(n: int) -> str:
    if n > 0:
        print("So duong")
    elif n < 0:
        print("So am")
    else:
        print("So 0")
        
print(check_number(n))