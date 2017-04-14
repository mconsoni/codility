#!/usr/bin/env python2.7

def sieve(n):
	sieve = [True] * (n + 1)
	sieve[0] = sieve[1] = False
	i=2
	while (i * i <= n):
		if (sieve[i]):
			k = i * i
			while (k <= n):
				sieve[k] = False
				k += i
		i += 1

	primes = []
	for c in xrange(n+1):
		if sieve[c]:
			primes.append(c)
	return primes

def solution(N, P, Q):
	# Calcular los primos hasta N
	primos = sieve(N)

	# Calcular semiprimos hasta N
	semiprimos = []
	for c in xrange(0, len(primos)):
		if primos[c] * primos[c] > N:
			break
		for x in xrange(0, len(primos)):
			if primos[c] * primos[x] > N:
				break;
			semiprimos.append(primos[c] * primos[x])
	semiprimos = sorted(list(set(semiprimos)))

	n_semiprimos = [ 0 ] * N
	for c in xrange(len(semiprimos)):
		n_semiprimos[semiprimos[c] - 1] = c + 1
	last = 0
	for c in xrange(N):
		if n_semiprimos[c] == 0:
			n_semiprimos[c] = last
		else:
			last = n_semiprimos[c]
	print `n_semiprimos`
		
	# [0, 0, 0, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 6, 6, 6, 7, 8, 8, 8, 9, 10]
	ret = []
	for c in xrange(len(P)):
		ret.append(n_semiprimos[Q[c] - 1] - n_semiprimos[max(0, P[c] - 2)])

	return ret

		

print `solution(26, [1, 4, 16], [26, 10, 20])`
