#!/usr/bin/env python2.7

def solution(A):
	i = 1
	result = 0
	while (i * i < A):
		if (A % i == 0):
			result += 2
		i += 1
	if (i * i == A):
		result += 1
	return result
	

print `solution(24)`
