import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = []
chart = [[int(i)] for i in range(1,n+1)]
for i in range(n):
    z = [c-1 for c in list(map(int,input().split()))][2:]
    graph.append(z)
time = 0

def dfs(nod):
    global graph
    global time
    #break condition
    if len(chart[nod]) != 1:
        return 
    #end condition not necessary
    #if not graph[nod]:
    #    time += 1
    #    chart[nod].append(time)
    #    return
    # command
    time += 1
    chart[nod].append(time)
    
    # move
    for dis in graph[nod]:
            dfs(dis)

    # post-command
    time += 1
    chart[nod].append(time)
for i in range(n):
    dfs(i)
for i in range(n):
    print(*chart[i])
