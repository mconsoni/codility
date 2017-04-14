#!/usr/bin/env python2.7

def solution(A):
	n = len(A)
	size = 0
	for k in xrange(n):
		if (size == 0):
			size += 1
			value = A[k]
		else:
			if (value != A[k]):
				size -= 1
			else:
				size += 1
	candidate = -1
	if (size > 0):
		candidate = value
	leader = -1
	count = 0
	for k in xrange(n):
		if (A[k] == candidate):
			count += 1
	if (count > n // 2):
		leader = candidate
	for k in xrange(n):
		if (A[k] == leader):
			return k
	return -1


print `solution([4, 3, 4, 4, 4, 2])`
print `solution([4, 4, 3, 4, 4, 4, 2])`
print `solution([1, 3, 4, 4, 3, 4, 4, 4, 2])`
