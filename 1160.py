import sys
sys.setrecursionlimit(10**6)

w=0;h=0;
def dfs(x,y,Map):
    #ending condition
    if not (0 <= x and x < h and 0 <= y and y < w):
        return
    if Map[x][y] == 0:
        return
    
    #operation
    Map[x][y] = 0

    #moving deep
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            dfs(x+i,y+j,Map)

def start_cnt():
    global w,h
    w,h = map(int,input().split())
    if w == 0 and h == 0:exit();
    cnt = 0
    Map = []
    for i in range(h):
            Map.append(list(map(int,input().split())))
    for i in range(h):
        for j in range(w):
            if Map[i][j] == 1:
                dfs(i,j,Map)
                cnt += 1
    print(cnt)
while True:
    start_cnt()
