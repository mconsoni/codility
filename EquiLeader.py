#!/usr/bin/env python2.7

def goldenLeader(A):
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
	return leader


def solution(A):
	n = len(A)
	count = 0

	leader = goldenLeader(A)

	for c in range(n):
		if A[c] == leader:
			count += 1
		if count > n // 4:
			return c
	return -1


print `solution([4, 3, 4, 4, 4, 2])`
print `solution([4, 4, 3, 4, 4, 4, 2])`
print `solution([1, 3, 4, 4, 3, 4, 4, 4, 2])`
