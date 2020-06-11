def bs(a,s):
    l = 0
    r = len(s)
    while l < r:
        m = (l+r)//2
        if s[m] == a:
            return True
        elif s[m] > a:
            r = m
        else:
            l = m + 1
    return False

n = int(input())
s = list(map(int,input().split()))
q = int(input())
X = list(map(int,input().split()))

ans = 0
for x in X:
    if bs(x,s):
        ans += 1
print(ans)
