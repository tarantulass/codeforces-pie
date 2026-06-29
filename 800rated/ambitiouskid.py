"""
question
1. A and B, A being father asks B a question
2. B is given an array it has to return min no. of operations for cum pod =0
3. in this operation are either increase or decrease by 1
"""

"""
attempts
1. just get min of absolute!
"""
import math
n = int(input())
minval = math.inf
arr = list(map(int, input().split()))

for i in range(n):
	minval = min(minval, abs(arr[i]))

print(minval)
