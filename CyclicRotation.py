#!/usr/bin/env python2.7

A_test = [3, 8, 9, 7, 6]
K_test = 3

def solution(A, K):
	for c in range(0, K):
		A = [A[len(A) - 1]] + A[0:-1]
	return(A)

print(str(A_test))
print(str(K_test))

sol = solution(A_test, K_test)
print(str(sol))
sol = solution(A_test, 0)
print(str(sol))
sol = solution([], 0)
print(str(sol))
