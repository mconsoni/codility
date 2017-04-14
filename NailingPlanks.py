#!/usr/bin/env python2.7


def solution(A, B, C):
	# Sort C
	nails = sorted(enumerate(C), key=lambda var: var[1])

	n = len(A)
	beg = 0
	end = n - 1
	result = -1
	while (beg <= end):
		mid = (beg + end) / 2
		if (A[mid] <= x):
			beg = mid + 1
			result = mid
		else:
			end = mid - 1
		



sol = solution([4, 4, 5, 5, 1], [3, 2, 4, 3, 1])
print(str(sol))
