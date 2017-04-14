#!/usr/bin/env python2.7

def solution(X, Y, D):
	dist = Y - X
	jumps = dist // D
	if jumps * D >= dist:
		return jumps
	else:
		return jumps + 1

sol = solution(10, 85, 30)
print(str(sol))
sol = solution(10, 100, 10)
print(str(sol))
sol = solution(10, 25, 10)
print(str(sol))
