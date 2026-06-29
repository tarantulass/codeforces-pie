"""
question
1. given an array a
2. we have to choose an x - aim 
3. this x when calculated like b1^b2^...  = 0
"""

"""
attempts
1. if cum xor of entire array is the same as x then yes else no
"""

t = int(input())

for i in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	cumxor = arr[0]
	for i in range(1,n):
		cumxor^=arr[i]

	if n%2==1:
		# here we need x to be same as cumxor
		print(cumxor)
	else:
		if cumxor!=0:
			print(-1)
		else:
			print(0)
		# as in even x will also be xored evetimes !!

