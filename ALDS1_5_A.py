import bisect
n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))
n_list.sort()

long_list = []
for j in range(1<<n):
    ans = 0
    for z in range(n):
        if (j>>z)&1:
            ans += n_list[z]
    long_list.append(ans)

long_list.sort()

#print((long_list))

for j in range(m):
    num = bisect.bisect_left(long_list,m_list[j])
    
    if num <= len(long_list) - 1 and long_list[num] == m_list[j]:
        print("yes")
    else:
        print("no")
