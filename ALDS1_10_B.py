INF = float('inf')
mm = [(-1,-1)]
n = int(input())
for _ in range(n):
    mm.append(tuple((map(int,input().split()))))

def scala(a,b,c):
    return mm[a][0] * mm[b][1] * mm[c][1] 

dp = [[INF for _ in range(n+1)] for _ in range(n+1)]
#init
for i in range(1,n):
    dp[i][i+1] = mm[i][0] * mm[i+1][1] * mm[i][1]
    dp[i][i] = 0
dp[-1][-1] = 0
#begin dp
for d in range(2,n):
    for l in range(1,n-d+1):
        r = l + d
        for m in range(l,r):
            dp[l][r] = min(dp[l][m] + dp[m+1][r] + scala(l,r,m), dp[l][r])
print(dp[1][n])
for d in range(2,n):
    for l in range(1,n-d+1):
        r = l + d
        for m in range(l,r):
            dp[l][r] = max(dp[l][m] + dp[m+1][r] + scala(l,r,m), dp[l][r])

print(dp[1][n])
