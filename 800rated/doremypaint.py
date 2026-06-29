"""
question
1. given an array of positive integers of length n
2. aim is to know whether we can have adjacent pair sum equal to k
3. k is not given in there!!
4. interestingly we can rearrange the array for matching the desried criteria
"""

"""
attempts
1. obviously 1st thought is of an AP to follow this - O(N) to check if array is an AP
2. an example of 1 1 2 shows there are more possiblities than just AP
"""

from collections import Counter
t = int(input())

for i in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	res = []
	# ALTERNATE ELEMENTS NEED TO BE SAME !!
	# EVERY ODD POSITON MUST HAVE SAME VALUE EVERY EVEN MUST HAVE SAME
	# 1 2 1 OR 1 4 1 4 1
	freq = Counter(arr)
	if len(freq)>2:
		print("No")
	elif len(freq)==1:
		print("Yes")
	else:
		for i, j in freq.items():
			res.append(j)
		a, b = res[0], res[1]
		if n%2==1 and abs(a-b)==1:
			print("Yes")
			continue
		if n%2==0 and abs(a-b)==0:
			print("Yes")
			continue
		# contnue very importnat else NO also gets printed
		# no need to add anotehr varibale again and again
		# if above condiions failed then NO
		print("No")

