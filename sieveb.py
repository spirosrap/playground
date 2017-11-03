#!/usr/bin/env python

from math import ceil,sqrt
import sys

def sieve(n1,n2):
	n = n2
	A = [True]*(n + 1)
	for i in range(2,ceil(sqrt(n)+1)):
		if A[i]:
			for j in range(i*i,n+1,i):
				A[j] = False
	return([i for i in range(len(A)) if A[i]== True and i >= n1])


if __name__ == "__main__":
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    assert n2 > n1,"Please enter a valid range, for example 10-100"
    try:
    	print(sieve(n1,n2))
    except:
    	print("Please use the script like this \"./sieveb 100 1000")
