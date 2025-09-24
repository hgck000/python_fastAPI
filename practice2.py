#!/usr/bin/env python3
import math
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(a: int, b: int) -> list[int]:
    list_primes = []
    for n in range(a, b + 1):
        if is_prime(n):
            list_primes.append(n)
    return list_primes

print(count_primes(int(input("Nhập a: ")), int(input("Nhập b: "))))
    