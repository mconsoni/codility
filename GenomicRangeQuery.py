#!/usr/bin/env python2.7

def solution2(S, P, Q):
	str = []
	for c in S:
		if c == 'A':
			str.append(1)
		elif c == 'C':
			str.append(2)
		elif c == 'G':
			str.append(3)
		elif c == 'T':
			str.append(4)

	ret = [ 4 ] * len(P)
	for c in range(0, len(P)):
		for a in str[P[c]:Q[c] + 1]:
			if ret[c] > a:
				ret[c] = a
			
	return ret	

def writeCharToList(S, last_seen, c, idx):
    if S[idx] == c:
        last_seen[idx] = idx
    elif idx > 0:
        last_seen[idx] = last_seen[idx -1]
 
def solution(S, P, Q):
     
    if len(P) != len(Q):
        raise Exception("Invalid input")
     
    last_seen_A = [-1] * len(S)
    last_seen_C = [-1] * len(S)
    last_seen_G = [-1] * len(S)
    last_seen_T = [-1] * len(S)
         
    for idx in xrange(len(S)):
        writeCharToList(S, last_seen_A, 'A', idx)
        writeCharToList(S, last_seen_C, 'C', idx)
        writeCharToList(S, last_seen_G, 'G', idx)
        writeCharToList(S, last_seen_T, 'T', idx)

    print `last_seen_A`
    print `last_seen_C`
    print `last_seen_G`
    print `last_seen_T`
     
     
    solution = [0] * len(Q)
     
    for idx in xrange(len(Q)):
        if last_seen_A[Q[idx]] >= P[idx]:
            solution[idx] = 1
        elif last_seen_C[Q[idx]] >= P[idx]:
            solution[idx] = 2
        elif last_seen_G[Q[idx]] >= P[idx]:
            solution[idx] = 3
        elif last_seen_T[Q[idx]] >= P[idx]:
            solution[idx] = 4
        else:    
            raise Exception("Should never happen")
         
    return solution
		 

S_t = 'CAGCCTA'
P_t = [ 2, 5, 0 ]
Q_t = [ 4, 5, 6 ]
sol = solution(S_t, P_t, Q_t)
print(str(sol))
