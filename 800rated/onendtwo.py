"""
question
1. given a sequence of all 1's and 2's
2. find integer k for which cum prod till k == cum prod after k
3. print smallest k if exists!!
"""

"""
attempts
1. CLEARLY cum prod of entire has to be a squared number!!
2. but we cant be sure if this till k is satisifed just by squared numbers
3. luckily we only have 1 and 2 in entire array!!
4. but we want to return this index k !!
"""
import math
t = int(input())

for i in range(t):
	n = int(input())
	arr = list(map(int, input().split()))

	cumprod = 1
	for i in arr:
		cumprod*=i
	root = math.sqrt(cumprod)

	# if not perfect sqaure then !!
	if root*root!=cumprod:
		print(-1)
		continue

	# sqaured number check is this !
	index = 1 # 1 based
	num = 1
	while index<=n:
		num*=arr[index-1]
		if num==root:
			print(index)
			break
			# not continue !!
		index+=1
