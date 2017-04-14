#!/usr/bin/env python2.7

def solution(S):
    stack = []
     
    for symbol in S:
        if symbol == '(':
            stack.append(symbol)
        else:
            if len(stack) == 0:
                return 0
            stack.pop()
     
    if len(stack) != 0:
        return 0
             
    return 1

		
assert solution("(()(())())") == 1
assert solution("())") == 0
