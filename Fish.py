#!/usr/bin/env python2.7

def solution(A, B):
	stack = []
	alive = 0
	for c in xrange(len(A)):
		if B[c] == 0:
			# arriba
			while len(stack) != 0:
				if A[c] > stack[-1]:
					stack.pop()
				else:
					break
			if len(stack) == 0:
				alive += 1
		else:
			# abajo
			stack.append(A[c])

	alive += len(stack)

	return alive
		     

print `solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0])`
