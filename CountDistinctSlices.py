#!/usr/bin/env python2.7


def solution(M, A):
	the_sum = 0
	front = back = 0
	seen = [False] * (M+1)

	print '--- INIT ---'
	print 'A: ' + `A`
	print 'the_sum: ' + `the_sum`
	print 'front: ' + `front`
	print 'back: ' + `front`
	print 'seen: ' + `seen`

	while (front < len(A) and back < len(A)):
		print '--- WHILE 1 ---'
		print 'A: ' + `A`
		print 'the_sum: ' + `the_sum`
		print 'front: ' + `front`
		print 'back: ' + `front`
		print 'seen: ' + `seen`

		while (front < len(A) and seen[A[front]] != True):
			print '--- WHILE 2 ---'
			print 'A: ' + `A`
			print 'the_sum: ' + `the_sum`
			print 'front: ' + `front`
			print 'back: ' + `front`
			print 'seen: ' + `seen`

			the_sum += (front-back+1)
			seen[A[front]] = True
			front += 1
		else:
			print '--- ELSE WHILE 2 ---'
			print 'A: ' + `A`
			print 'the_sum: ' + `the_sum`
			print 'front: ' + `front`
			print 'back: ' + `front`
			print 'seen: ' + `seen`

			while front < len(A) and back < len(A) and A[back] != A[front]:
				print '--- WHILE 32 ---'
				print 'A: ' + `A`
				print 'the_sum: ' + `the_sum`
				print 'front: ' + `front`
				print 'back: ' + `front`
				print 'seen: ' + `seen`

				seen[A[back]] = False
				back += 1
				 
			seen[A[back]] = False
			back += 1

	print '--- END ---'
	print 'A: ' + `A`
	print 'the_sum: ' + `the_sum`
	print 'front: ' + `front`
	print 'back: ' + `front`
	print 'seen: ' + `seen`
				 
	return min(the_sum, 1000000000)  
		


sol = solution(6, [3, 4, 5, 5, 2])
print(str(sol))
