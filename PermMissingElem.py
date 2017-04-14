#!/usr/bin/env python2.7

def solution(A):
	l = len(A)
	tot = ((l + 1) * (l + 2)) / 2
	for c in range(0, l):
		tot = tot - A[c]
	return tot


A_test = [ 2, 3, 1, 5 ]
sol = solution(A_test)
print `sol`

A_test = [ 1, 2, 3, 4, 5, 7 ]
sol = solution(A_test)
print `sol`
