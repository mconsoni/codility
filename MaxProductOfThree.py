#!/usr/bin/env python2.7


def solution(A):
	A.sort()
	return max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])
		
		
A_t = [ -3, 1, 2, -2, 5, 6 ]
sol = solution(A_t)
print(str(sol))
