#!/usr/bin/env python2.7

test = [ 9, 3, 9, 3, 9, 7, 9 ]

def solutionM(array):
	if len(array) == 0:
		return -1
	for t in array:
		if array.count(t) % 2 == 1:
			return t
	return -1


# This problem can be found in many algorithm books. A xor A cancels itself and B xor 0 is B. Therefore A xor A xor B xor C xor C is B.
def solution(A):
	missing_int = 0
	for value in A:
		missing_int ^= value
	return missing_int

sol = solution(test)
print(str(sol))
