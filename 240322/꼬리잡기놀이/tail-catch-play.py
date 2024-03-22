from collections import deque
n,m,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
groups = [deque()*(m) for _ in range(m)]
groups_n = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]
v = [[False] * n for _ in range(n)]

# 그룹 찾기 함수
def bfs(i,j,groups_n):
    q = deque()
    q.append((i,j))
    v[i][j] = True
    groups[groups_n].append((i,j))
    while q:
        ci, cj = q.popleft()
        for i in range(4):
            ni,nj = ci+dx[i], cj+dy[i]
            if 0<=ni<n and 0<=nj<n:
                if not v[ni][nj]:
                    if arr[ni][nj] ==2 or arr[ni][nj]==3: # 2번이면 계속 포함
                        q.append((ni,nj))
                        v[ni][nj] = True
                        groups[groups_n].append((ni,nj))


# 그룹 맺기
for _ in range(m):
    for i in range(n):
        for j in range(n):
            if not v[i][j] and arr[i][j] == 1:
                bfs(i,j,groups_n)
                groups_n += 1

def move():
    for group in groups:
        x,y = group.pop() # 꼬리 만들기
        arr[x][y] = 4 # 선로로 돌리기
        arr[group[-1][0]][group[-1][1]] = 3 # 새로운 꼬리

        x,y = group[0]
        arr[x][y] = 2 # 머리를 몸통으로
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and arr[nx][ny] == 4:
                arr[nx][ny] = 1
                group.appendleft((nx,ny))
                break

def ball(round): # return은 (-1,-1) 즉 좌표로 해서, 큐에 접근하여 뒤바꿀 기차와 점수 알아내기
    round %=4*n
    if round < n:
        for j in range(n):
            if arr[round][j] in (1,2,3): return (round,j)
    elif round < 2*n:
        for i in range(n):
            if arr[n-1-i][round-n] in (1,2,3): return (n-1-i,round-n)
    elif round < 3*n:
        for j in range(n):
            if arr[3*n-1-round][n-1-j] in (1,2,3): return (3*n-1-round,n-1-j)
    else:
        for i in range(n):
            if arr[i][4*n-1-round] in (1,2,3): return (i,4*n-1-round)
    return (-1,-1)

def change(x,y):
    if (x,y) == (-1,-1): return 0

    for i in range(m):
        if (x,y) in groups[i]:
            for j in range(len(groups[i])):
                if groups[i][j] == (x,y):
                    arr[groups[i][0][0]][groups[i][0][1]] = 3
                    arr[groups[i][-1][0]][groups[i][-1][1]] = 1
                    groups[i].reverse()
                    return (j+1) ** 2
cnt = 0

for i in range(k):
    move()
    a,b = ball(i)
    cnt += change(a,b)
print(cnt)