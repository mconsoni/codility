#!/usr/bin/env python2.7

def increase(X, counters):
	counters[X - 1] = counters[X - 1] + 1

def maxCounter(counters):
	m = max(counters)
	return [ m ] * len(counters)

def solution(N, A):
	counters = [ 0 ] * N
	last = 0
	max = 0
	for a in A:
		if a >= 1 and a <= N:
			if counters[a - 1] < last:
				counters[a - 1] = last
			counters[a  - 1] += 1
			if counters[a - 1] > max:
				max = counters[a - 1]
			#increase(a, counters)
		elif a == N + 1:
			last = max
			#counters = maxCounter(counters)

	for n in range(0, N): 
		if counters[n] < last:
			counters[n] = last

	return counters


A_test = [ 3, 4, 4, 6, 1, 4, 4 ]
N_test = 5
sol = solution(N_test, A_test)
print(str(sol))
