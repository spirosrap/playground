#!/usr/bin/env python

from math import ceil,sqrt
import sys
import numpy as np
def sieve(n1,n2):
	n = n2
	A = [True]*(n + 1)
	for i in range(2,ceil(sqrt(n)+1)):
		if A[i]:
			for j in range(i*i,n+1,i):
				A[j] = False
	primes = [i for i in range(len(A)) if A[i]== True and i >= n1]
	gap = [primes[i+1] - primes[i] for i in range(len(primes) - 1)]

	# Returns the average "space" between consecutive primes
	return np.average(np.array(gap))

if __name__ == "__main__":
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    assert n2 > n1,"Please enter a valid range, for example 10-100"
    print(sieve(n1,n2))
