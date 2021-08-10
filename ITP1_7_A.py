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
def stdi():
	return sys.stdin.readline().rstrip().split()
prn = lambda x: print(*x, sep='\n')
prn1 = lambda x: print(*x, sep='')
while True:
	a = [int(x) for x in stdi()]
	m = a[0]; f = a[1]; r = a[2]
	if m == -1 and f == -1 and r == -1:
		exit(0)
	if m == -1 or f == -1 or m + f<30:
		print("F")
	elif m + f >= 80:
		print("A")
	elif 65 <= m+f <80:
		print("B")
	elif 50 <= m+f < 65:
		print("C")
	elif 30 <= m+f < 50:
		if 50 <= r:
			print("C")
		else:
			print("D")
