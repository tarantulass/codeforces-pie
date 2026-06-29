"""
question
1. aim is to desort the array
2. add 1 to elements in index {1,n-1} and subtract from {2,n}
3. return min number of operations to desort the array
given array need not be sorted already
"""

"""
attempts
1. pick the min difference adjacent element
"""

import math
t = int(input())

for i in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	mindiff = math.inf
	desorted = False
	for j in range(n-1):
		mindiff = min(mindiff, arr[j+1]- arr[j])
		if mindiff<0:
			# this means array not sorted hence we say no operations needed
			desorted = True
			break
	if desorted:
		print(0)
		continue
	ops = mindiff//2 + 1
	# here mindiff//2 for + and - and 1 for making them desorted
	print(ops)
