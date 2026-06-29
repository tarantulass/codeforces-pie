"""
question
1. given string x and s of length n and m all lowercase
2. min operations to apply on x only
3. return min no. of operations to have s as a sibstring in  x
4. operations are only appending current value of x again to it 
"""

"""
attempts
1. simple append and check
importantly we have to notice that s can be either inside already or can be 
across hence we need this 2*m check here
"""

t = int(input())

for i in range(t):
	n,m = map(int, input().split())
	x = input()
	s = input()
	
	ops = 0
	newlength = 0
	inside = False
	# if already in x
	if s in x:
		print(0)
		inside = True

	while newlength<=2*m and not inside:
		x+=x
		newlength = len(x)
		ops+=1

		if newlength>=m and s in x:
			print(ops)
			inside = True
			break


	if not inside:
		print(-1)
