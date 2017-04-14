#!/usr/bin/env python2.7

def solution(A):
	west = 0;
	for a in A:
		if a == 1:
			west += 1

	count = 0
	for c in range(0, len(A)):
		if count > 1000000000:
			return -1
		if A[c] == 0:
			count += west
		else:
			west -= 1
		
	return count
		
		 

A_t = [ 0, 1, 0, 1, 1 ]
sol = solution(A_t)
print(str(sol))
A_t = [ 1, 0, 1, 1 ]
sol = solution(A_t)
print(str(sol))
A_t = [ 1, 1, 0, 1, 1 ]
sol = solution(A_t)
print(str(sol))
A_t = [ 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]
sol = solution(A_t)
print(str(sol))
