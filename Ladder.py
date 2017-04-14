#!/usr/bin/env python2.7

def solution2(A, B):
	for c in xrange(len(A)):
		steps = A[c]
		l = B[c]
		

def solution(A, B):
	L = max(A)
 
	fib = [0] * (L+2)
	fib[1] = 1
	for i in xrange(2, L + 2):
		fib[i] = (fib[i-1] + fib[i-2]) % (1 << 30)
 
	return_arr = [0] * len(A)
 
	for idx in xrange(len(A)):
		return_arr[idx] = fib[A[idx]+1] & ((1 << B[idx]) - 1)
 
	return return_arr
		



sol = solution([4, 4, 5, 5, 1], [3, 2, 4, 3, 1])
print(str(sol))
