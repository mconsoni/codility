#!/usr/bin/env python2.7

def solution(A):
	i = 1
	result = 0
	# divisors = []
	minPer = 1000000000 * 2 + 2
	while (i * i < A):
		if (A % i == 0):
			# divisors.append(i)
			# divisors.append(A / i)
			minPer = min(minPer, 2 * (i + (A / i)))
			result += 2
		i += 1
	if (i * i == A):
		# divisors.append(i)
		result += 1

	# divisors.sort()
	# print `divisors`
	
	return minPer

import math
def solution2(N):
    if N <= 0:
      return 0
   
    print `math.sqrt(N)`
    print `int(math.sqrt(N))`
    print `range(int(math.sqrt(N)), 0, -1)`
    # Buscar el primo mas grande
    for i in xrange(int(math.sqrt(N)), 0, -1):
        if N % i == 0:
            return 2*(i+N/i)
             
    raise Exception("should never reach here!") 
	

print `solution(30)`
print `solution2(30)`
print `solution(31)`
print `solution2(31)`
print `solution(32)`
print `solution2(32)`
