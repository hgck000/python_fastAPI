#!/usr/bin/env python3
import math

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
        


def grade(score: float) -> str:
    if score < 0 or score > 10:
        return "Điểm không hợp lệ"
    if score >= 8.5:
        return "Giỏi"
    elif score >= 7.0 and score <= 8.5:
        return "Khá"
    elif score >= 5.0 and score <= 7.0:
        return "Trung bình"
    else:
        return "Yếu"
    

def is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    elif year & 100 == 0:
        return False
    elif year % 4  == 0:
        return True
    else:
        return False
