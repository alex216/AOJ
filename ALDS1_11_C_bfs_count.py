from collections import deque
graph = []
n = int(input())
dist = [[int(c),-1] for c in range(1,n+1)]
process_q = deque()
for i in range(n):
    graph.append([c-1 for c in list(map(int,input().split()))][2:])

def bfs():
    while len(process_q) > 0:
        parent = process_q.popleft()
        for child in graph[parent]:
            if dist[child][1] != -1:
                continue
            process_q.append(child)
            dist[child][1] = dist[parent][1] + 1

process_q.append(0)
dist[0][1] = 0
bfs()

for element in dist:
    print(*element)
