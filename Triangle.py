#!/usr/bin/env python2.7


def solution(A):
	# Array de los indices de los valores en orden
	indices = sorted(range(len(A)), key = lambda x:A[x])

	A.sort()
	print `A`
     
	for i in xrange(len(A)-2):
		if A[i] + A[i+1] > A[i+2]:
			return 1
             
	return 0

		
		
A_t = [ 10, 2, 5, 1, 8, 20 ]
sol = solution(A_t)
print(str(sol))

A_t = [ 1, 1, 2, 3, 5, 8 ]
sol = solution(A_t)
print(str(sol))
