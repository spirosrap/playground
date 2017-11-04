#!/usr/bin/env python

from math import ceil,sqrt
import sys
import numpy as np

def aktinsieve(limit):
    """ Returns  a list of primes < n """
    sieve = [False] * limit
    for x in range(1,ceil(sqrt(limit))):
    	for y in range(1,ceil(sqrt(limit))):
    		n = 4*x**2 +y**2
    		if(n<=limit and (n%12==1 or n%12 ==5)):
    			sieve[n] = not(sieve[n])
    		
    		n = 3*x**2 + y**2
    		if(n<=limit and n%12 == 7):
    			sieve[n] = not(sieve[n])

    		n = 3*x**2 - y**2
    		if(x>y and n<=limit and n%12 == 11):
    			sieve[n] = not(sieve[n])

    for r in range(5,ceil(sqrt(limit))):
    	if(sieve[r]):
    		for i in range(r**2,limit,r**2):
    			sieve[i] = False
    primes = [i for i in range(limit) if sieve[i]]		
    return [2,3] + primes

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(aktinsieve(n))
