#!/usr/bin/env python2.7


# For large integers
# O(log(n))
def gcdL(a, b, res):
	if a == b:
		return res * a
	elif (a % 2 == 0) and (b % 2 == 0):
		return gcd(a // 2, b // 2, 2 * res)
	elif (a % 2 == 0):
		return gcd(a // 2, b, res)
	elif (b % 2 == 0):
		return gcd(a, b // 2, res)
	elif a > b:
		return gcd(a - b, b, res)
	else:
		return gcd(a, b - a, res)


# O(log(p + q))
def gcd(p, q):
	if q == 0:
		return p
	return gcd(q, p % q)
 

def hasSameFactors(p, q):
	if p == q == 0:
		print 'True'
		return True
	 
	denom = gcd(p,q)
	print 'P: ' + `p` + ' Q: ' + `q` + ' denom: ' + `denom` 
	 
	while (p != 1):
		p_gcd = gcd(p,denom)
		print 'P: ' + `p` + ' Q: ' + `q` + ' p_gcd: ' + `p_gcd` 
		if p_gcd == 1:
			break
		p /= p_gcd
	else:
		print 'P: ' + `p` + ' Q: ' + `q`
		while (q != 1):
			q_gcd = gcd(q,denom)
			print 'Q: ' + `q` + ' P: ' + `p` + ' q_gcd: ' + `q_gcd` 
			if q_gcd == 1:
				break
			q /= q_gcd
		else:
			print 'True'
			return True
	 
	print 'False'
	return False
 
 
def solution(A, B):
	if len(A) != len(B):
		raise Exception("Invalid input")
	cnt = 0
	for idx in xrange(len(A)):
		if A[idx] < 0 or B[idx] < 0:
			raise Exception("Invalid value")
		if hasSameFactors(A[idx], B[idx]):
			cnt += 1
	 
	return cnt

	


print `solution([ 75 ], [ 15 ])`
print `solution([ 15, 10, 3 ], [ 75, 30, 5 ])`
