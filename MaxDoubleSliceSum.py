#!/usr/bin/env python2.7

def solution(A):
	# MAX SLICE
	# max_ending = max_slice = 0
	# for a in A:
	# 	max_ending = max(0, max_ending + a)
	# 	max_slice = max(max_slice, max_ending)
	# return max_slice

    ending_here = [0] * len(A)
    starting_here = [0] * len(A)
     
    for idx in xrange(1, len(A)):
        ending_here[idx] = max(0, ending_here[idx-1] + A[idx])
     
    for idx in reversed(xrange(len(A)-1)):
        starting_here[idx] = max(0, starting_here[idx+1] + A[idx])
     
    max_double_slice = 0
     
    for idx in xrange(1, len(A)-1):
        max_double_slice = max(max_double_slice, starting_here[idx+1] + ending_here[idx-1])
         
         
    return max_double_slice


print `solution([3, 2, 6, -1, 4, 5, -1, 2])`
