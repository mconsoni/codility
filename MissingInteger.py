#!/usr/bin/env python2.7

def solution(A):
	dic = {}
	for a in A:
		dic[a] = 1;
	kk = dic.keys()
	vv  = sorted(kk)
	prev = 0;
	for k in vv:
		if (prev + 1) != k:
			return prev + 1
		prev = prev + 1
	return prev + 1



A_test = [ 1, 3, 6, 4, 1, 2 ]
sol = solution(A_test)
print(str(sol))

A_test = [ 1, 3, 6, 4, 5, 2 ]
sol = solution(A_test)
print(str(sol))

A_test = [ 1, 3, 6, 4, 5, 3 ]
sol = solution(A_test)
print(str(sol))
