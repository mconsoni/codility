#!/usr/bin/env python2.7


def solution(A):
    circle_endpoints = []
    for i, a in enumerate(A):
        circle_endpoints += [(i-a, True), (i+a, False)]
 
    circle_endpoints.sort(key=lambda x: (x[0], not x[1]))
 
    intersections, active_circles = 0, 0
 
    for _, is_beginning in circle_endpoints:
        if is_beginning:
            intersections += active_circles
            active_circles += 1
        else:
            active_circles -= 1
        if intersections > 10E6:
            return -1
 
    return intersections

		
assert solution([1, 5, 2, 1, 4, 0]) == 11
assert solution([]) == 0
assert solution([0,1]) == 1
assert solution([0, 0]) == 0
assert solution([1,0,0,3]) == 4
#print 'Ok!'	
