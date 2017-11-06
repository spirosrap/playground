#!/usr/bin/env python

from math import ceil,sqrt
import sys

def sieve(n):
	A = [True]*(n + 1)
	for i in range(2,ceil(sqrt(n)+1)):
		if A[i]:
			for j in range(i*i,n+1,i):
				A[j] = False
	return([i for i in range(len(A)) if A[i]== True][2:])


if __name__ == "__main__":
    a = int(sys.argv[1])
    try:
    	print(sieve(a))
    except:
    	print("Please use the script like this \"./sieve 100")
