"""
2 players A and B
operations either increase or decrease the number
A starts and if after A move numebr os divisible by 3 A wins else if after 10 moves B wins
both play optimally
"""
"""
solution
as from 3k+1, 3k+2 playing optimally A can win as he has to make it 3k or 3k+3
on the otherhand for 3k he makes it 3k+1 or 3k-1 so then B makes it 3k again
"""

# btw only 3 kinds of integers 
# 1. 3k, 3k+1, 3k+2

t = int(input())

for i in range(t):
	n = int(input())
	if n%3==0:
		print("Second")
	else:
		print("First")
