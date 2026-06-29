"""
question
1. given 3 integers n a b
2. defintiion of permutation of length n is array containing each integer from 1 to n
3. return yes if there exists such permutations
"""

"""
attempts
1. simple observation
"""

t = int(input())

for i in range(t):
	n, a, b = map(int, input().split())
	if n>a+b+1 or (n==a and n==b):
		# the second conditon means we have exact same arrays
		print("Yes")
	else:
		print("No")

