#!/usr/bin/env python2.7

def solution(A):
	l = len(A)
	tot = (l * (l + 1)) / 2
	for c in range(0, l):
		tot = tot - A[c]

	if tot == 0:
		return 1 
	else:
		return 00


A_test = [ 4, 1, 3, 2 ]
sol = solution(A_test)
print `sol`

A_test = [ 4, 1, 3 ]
sol = solution(A_test)
print `sol`
