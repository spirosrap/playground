from math import ceil,sqrt
def sieve(n):
	A = [True]*(n + 1)
	for i in range(2,ceil(sqrt(n)+1)):
		if A[i]:
			for j in range(i*i,n+1,i):
				A[j] = False
	return([i for i in range(len(A)) if A[i]== True][2:])


print(sieve(100))
