#!/usr/bin/env python2.7

def create_peaks(A):
	N = len(A)
	peaks = [False] * N
	for i in xrange(1, N - 1):
		if A[i] > max(A[i - 1], A[i + 1]):
			peaks[i] = True
	return peaks

def next_peak(A):
	N = len(A)
	peaks = create_peaks(A)
	print `peaks`
	next = [0] * N
	next[N - 1] = -1
	for i in xrange(N - 2, -1, -1):
		if peaks[i]:
			next[i] = i
		else:
			next[i] = next[i + 1]
	return next

def solution(A):
	N = len(A)
	print `A`
	next = next_peak(A)
	print `next`
	i = 1
	result = 0
	while (i - 1) * i <= N:
		pos = 0
		num = 0
		while pos < N and num < i:
			pos = next[pos]
			if pos == -1:
				break
			num += 1
			pos += i
		result = max(result, num)
		i += 1
	return result


print `solution([ 1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2 ])`
