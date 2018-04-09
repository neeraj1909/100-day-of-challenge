#!/bin/python3

import sys

def sum_factors_of_n_below_k(k, n):
    m = (k -1) //n
    return n *m *(m+1) //2

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    total = 0
    #for multiple of 3
    total = total + sum_factors_of_n_below_k(n, 3)
    #for multiple of 5
    total = total + sum_factors_of_n_below_k(n, 5)
    #for multiple of 15
    total = total - sum_factors_of_n_below_k(n, 15)
    print("%s" % total)
