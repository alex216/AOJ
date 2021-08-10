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
	return stdin.readline().rstrip().split()
prn = lambda x: print(*x, sep='\n')
prn1 = lambda x: print(*x, sep='')
