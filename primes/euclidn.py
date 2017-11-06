#!/usr/bin/env python

from math import ceil,sqrt
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

import sys

def euclidn(n):
	A = [True]*(n + 1)
	en = []
	for i in range(2,ceil(sqrt(n)+1)):
		if A[i]:
			for j in range(i*i,n+1,i):
				A[j] = False
	e = [i for i in range(len(A)) if A[i]== True][2:]	
	j = 1
	for i in e:
		j*=i
		en.append(j+1)

	
	return en


if __name__ == "__main__":
    a = int(sys.argv[1])
    try:
    	print(euclidn(a))
    except:
    	print("Please use the script like this \"./euclidn 100")
