#!/usr/bin/env python2.7

import sys

if len(sys.argv) < 2:
	print('Use: ' + sys.argv[0] + ' <INT>')
	exit(1)


def int2bin(i):
    if i == 0: return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i /= 2
    return s



input = sys.argv[1]
#strInput = bin(int(input))[2:]
strInput = int2bin(int(input))

print(strInput)
max = 0
count = 0
for c in strInput:
	if c == '0':
		count = count + 1
	else:
		if count > max:
			max = count
		count = 0
if count > max:
	max = count
	

print(str(max))
