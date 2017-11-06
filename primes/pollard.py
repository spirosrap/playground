#!/usr/bin/env python

from math import ceil,sqrt
from fractions import gcd
import sys

def pollard(n):
	
	def g(x):
		return (x**2 + 1) % n
	x = 2
	y = 2
	d = 1
	while d == 1:
		x = g(x)
		y = g(g(y))
		d = gcd(abs(x-y),n)
		print(y)
	if d == n:
		return None
	else:
		return d


if __name__ == "__main__":
    a = int(sys.argv[1])
    try:
    	print(pollard(a))
    except:
    	print("Please use the script like this \"./pollard 100")
