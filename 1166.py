from collections import deque

def cat_go(x,y,nx,ny):
    if x == nx:
        return 1-wall[2*x][min(ny,y)]
    else:
        return 1-wall[2*min(x,nx)+1][y]

def bfs():
    global mapp
    mapp[0][0] = 1
    que = deque()
    que.append([0,0])
    while que:
        place = que.popleft()
        x = place[0];y = place[1]
        #end
        if x == h-1 and y == w-1:
            return mapp[x][y]
        for d in [[1,0],[0,1],[-1,0],[0,-1]]:
            nx = x + d[0];ny = y + d[1]
            #forbidden
            if not (0<=nx and nx<h and 0<=ny and ny<w):continue
            if not cat_go(x,y,nx,ny):continue
            #wont go
            if mapp[nx][ny] != 0:continue
            #go
            mapp[nx][ny] = mapp[x][y]+1
            que.append([nx,ny])
    return 0

while True:
    w,h = map(int,input().split())
    if w==0 and h==0:exit()
    mapp = [[0] * w for _ in range(h)]
    wall = []
    for i in range(2*h-1):
        wall.append(list(map(int,input().split())))
    print(bfs())
