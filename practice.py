#!/usr/bin/env python3

n = int(input("Enter your number:"))

def is_prime(n: int) -> bool:
    if n < 2:
        return False