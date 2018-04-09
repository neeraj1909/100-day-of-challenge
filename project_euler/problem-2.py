#!/bin/python3

import sys

def calculate_even_fibonacci_sum(n):
    a = 1
    b = 2
    even_fibonacci_total = b
    new_term = a + b

    while new_term < n:
        #new_term = a + b
        if new_term % 2 == 0:
            even_fibonacci_total = even_fibonacci_total + new_term

        a = b
        b = new_term
        new_term = a + b
    return even_fibonacci_total


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    total = calculate_even_fibonacci_sum(n)
    print("%d" % total)
