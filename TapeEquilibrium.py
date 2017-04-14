#!/usr/bin/env python2.7

def solution(A):
	pa = A[0];
	pb = 0;

	for c in range(1, len(A)):
		pb = pb + A[c]

	min = abs(pa - pb);

	for c in range(1, len(A)):
		pa = pa + A[c]
		pb = pb - A[c]
		if abs(pa - pb) < min:
			min = abs(pa - pb)

	return min 



A_test = [ 3, 1, 2, 4, 3 ]
sol = solution(A_test)
print `sol`

A_test = [ 3, 1, 2, 4, 3, 9 ]
sol = solution(A_test)
print `sol`
