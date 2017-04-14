#!/usr/bin/env python2.7

def solution(A):
    max_profit = 0
    min_day = 200000
     
    for day in A:
        min_day = min(min_day, day)
        max_profit = max(max_profit, day-min_day)
     
    return max_profit


a = [ 23171, 21011, 21123, 21366, 21013, 21367 ]
print `solution(a)`
