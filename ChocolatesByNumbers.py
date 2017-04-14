#!/usr/bin/env python2.7

def solutionAux(N, M, i, c):
	print `N`
	if N[i] == False:
		return c
	else:
		N[i] = False
		return solutionAux(N, M, (i + M) % len(N), c + 1)

def solution(N, M):
	N_ = [ True ] * N
	return solutionAux(N_, M, 0, 0)


def gcd(p, q):
	if q == 0:
		return p
	return gcd(q, p % q)
 
def lcm(p,q):
	return p * (q / gcd(p,q))
 
def solution2(N, M):
	return lcm(N,M)/M



print `solution(10, 4)`
print `solution2(10, 4)`
