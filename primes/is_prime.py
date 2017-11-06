#!/usr/bin/env python

from math import ceil,sqrt
import sys

def is_prime(n):
	if n<=1:
		return False
	elif n <= 3:
		return True
	elif n % 2 == 0 or n % 3 == 0:
		return False
	i = 5
	while i**2<=n:
		if n % i == 0 or n%(i+2) == 0:
			return False
		i+=6
	return True


if __name__ == "__main__":
    a = int(sys.argv[1])
    print(is_prime(a))