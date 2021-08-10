from collections import deque
from bisect import *
from collections import Counter
import math
import sys
from decimal import *
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9 + 7

def factors(n: int):
    l = []
    for i in range(2, int(n**0.5) + 1):

#factorization
#        if n%i==0:l.append(i); l.append(n//i)
#    return tuple(sorted(l))

#prime factorization
        while n % i == 0:
            n //= i
            l.append(i)
    if n > 1:
        l.append(n)
    return l

input = sys.stdin.readline
readall = sys.stdin.read
def readall():
    return list(map(int, readall().split()))
def inp():
    return int(input())
def inpl():
    return list(map(int,input().split()))
def inpm():
    return map(int,input().split())

prn = lambda x: print(*x, sep='\n')
prn1 = lambda x: print(*x, sep='')

dorm = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
n = inp()
for _ in range(n):
	a = inpl()
	dorm[a[0]-1][a[1]-1][a[2]-1] += a[3]
for i in range(4):
	for j in range(3):
		print(" ",end = "")
		for k in range(10):
			if k == 9:
				print(dorm[i][j][k],end ="")
				continue
			print(dorm[i][j][k],end = " ")
		print()
	if i < 3:
		print("#"*20)
