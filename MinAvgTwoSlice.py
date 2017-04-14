#!/usr/bin/env python2.7


def solution(A):
	min_idx = 0
	min_value = 10001

	for idx in xrange(0, len(A)-1):
		if (A[idx] + A[idx+1])/2.0 < min_value:
			min_idx = idx
			min_value = (A[idx] + A[idx+1])/2.0
		if idx < len(A)-2 and (A[idx] + A[idx+1] + A[idx+2])/3.0 < min_value:
			min_idx = idx
			min_value = (A[idx] + A[idx+1] + A[idx+2])/3.0

	return min_idx
		
		
		 

A_t = [ 4, 2, 2, 5, 1, 5, 8 ]
sol = solution(A_t)
print(str(sol))
