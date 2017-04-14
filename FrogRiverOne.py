#!/usr/bin/env python2.7

def solution(X, A):
	if A.count(X) <= 0:
		return -1

	pos = [100001] * X
	for c in range(0,len(A)):
		if A[c] <= X and pos[A[c] - 1] > A[c]:
			pos[A[c] - 1] = c
	max = 0
	for p in pos:
		if max < p:
			max = p
	return max



A_test = [ 1, 3, 1, 4, 2, 3, 5, 4 ]
X_test = 5
sol = solution(X_test, A_test)
print(str(sol))

A_test = [ 1, 3, 1, 4, 2, 3, 5, 4 ]
X_test = 4
sol = solution(X_test, A_test)
print(str(sol))

A_test = [ 1, 3, 1, 4, 2, 3, 5, 4 ]
X_test = 2
sol = solution(X_test, A_test)
print(str(sol))

A_test = [ 1, 3, 1, 4, 2, 3, 5, 4 ]
X_test = 1
sol = solution(X_test, A_test)
print(str(sol))
