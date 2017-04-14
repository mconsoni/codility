#!/usr/bin/env python2.7

def solution(A, B, K):
#	ret = 0
#	for a in range(A - 1, B + 1):
#		if a % K == 0:
#			ret += 1
#	return ret

	print 'A: ' + `A` + ' '  + 'B: ' + `B` + ' ' +  'K: ' + `K`
	
	# Primer divisible
	if A % K == 0:
		pd = A
	else:
		pd = A + K - (A % K)
	#print 'pd: ' + `pd`
	if pd > B:
		return 0

	ret = 1
	
	# Divisibles entre pd y B
	d = (B - pd) // K
	#print 'B - pd: ' + `B - pd`
	#print 'd: ' + `d`

	ret = ret + d

	return ret
	


sol = solution(6, 11, 2)
print(str(sol))
sol = solution(6, 12, 2)
print(str(sol))
sol = solution(5, 11, 2)
print(str(sol))
sol = solution(5, 12, 2)
print(str(sol))
sol = solution(4, 11, 3)
print(str(sol))
sol = solution(4, 12, 3)
print(str(sol))
