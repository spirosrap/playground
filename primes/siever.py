#!/usr/bin/env python

from math import ceil,sqrt
import sys
import numpy as np

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(primes(n))
