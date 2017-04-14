#!/usr/bin/env python2.7

def solution(A):
	stack = []
	blocks = 0

	if len(A) == 0:
		return 0

	for h in A:
		if len(stack) == 0:
			stack.append(h)
			continue

		while len(stack) != 0 and h < stack[-1]:
			stack.pop()
			blocks += 1

		if len(stack) == 0 or h > stack[-1]:
			stack.append(h)
				
	return blocks + len(stack)	


		
print `solution([8, 8, 5, 7, 9, 8, 7, 4, 8])`
print `solution([8, 8, 8])`
print `solution([8, 7, 8])`
print `solution([ 1 ])`
print `solution([])`
