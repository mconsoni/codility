#!/usr/bin/env python2.7


def solution(A):
	ret = 2000000000
	for c in xrange(len(A)):
		for x in xrange(c, len(A)):
			ret = min(ret, abs(A[c]+A[x]))
	return ret

def solution2(A):
	value = 2000000000
	front_ptr = 0
	back_ptr = len(A)-1
	A.sort()
	 
	while front_ptr <= back_ptr:
		value = min(value, abs(A[front_ptr] + A[back_ptr]))
		if abs(A[front_ptr]) > abs(A[back_ptr]):
			front_ptr += 1
		else:
			back_ptr -= 1
			 
	return value




sol = solution([-8, 4, 5, -10, 3])
print(str(sol))
