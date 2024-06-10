R,C,K = map(int,input().split())
arr = [[0] * C for _ in range(R+3)]
Exit = [[False] * C for _ in range(R+3)]
ans = 0
di, dj = [-1,0,1,0],[0,1,0,-1]

from collections import deque
# 4. BFS 함수
def bfs(i,j):
    q = deque()
    q.append((i,j))
    v = [[False] * C for _ in range(R+3)]
    v[i][j] = True
    result = i
    while q:
        ci,cj = q.popleft()
        for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if inrange(ni,nj) and not v[ni][nj] and ((arr[ci][cj] == arr[ni][nj]) or (Exit[ci][cj] and arr[ni][nj] > 0)):
                q.append((ni,nj))
                v[ni][nj] = True
                result = max(result,ni)
    return result

# 3. inrange 함수
def inrange(i,j):
    return 3<=i<R+3 and 0<=j<C

# 2. check 함수
def check(i,j):
    flag = 0<=j-1 and j+1<C and i+1<R+3
    flag = flag and arr[i - 1][j - 1] == 0
    flag = flag and arr[i - 1][j] == 0
    flag = flag and arr[i - 1][j + 1] == 0
    flag = flag and arr[i][j - 1] == 0
    flag = flag and arr[i][j] == 0
    flag = flag and arr[i][j + 1] == 0
    flag = flag and arr[i + 1][j] == 0
    return flag

# 1. down 함수
def down(i,j,dr,idx):
    # 1.1 남쪽 이동
    if check(i+1,j):
        down(i+1,j,dr,idx)
    # 1.2 서쪽 회전 이동
    elif check(i+1,j-1):
        down(i+1,j-1,(dr+3)%4,idx)
    # 1.3 동쪽 회전 이동
    elif check(i+1,j+1):
        down(i+1,j+1,(dr+1)%4,idx)
    # 1.4 가장 남쪽 도착
    else:
        # 1.4.1 몸의 일부가 숲 벗어남
        if not inrange(i-1,j) or not inrange(i+1,j):
            for ci in range(R+3):
                for cj in range(C):
                    arr[ci][cj] = 0
                    Exit[ci][cj] = False
        # 1.4.2 정령 이동
        else:
            global ans
            arr[i][j] = idx
            for k in range(4):
                ni,nj = i+di[k],j+dj[k]
                arr[ni][nj] = idx
            Exit[i+di[dr]][j+dj[dr]] = True
            ans += bfs(i,j) - 3 + 1

for idx in range(1,K+1):
    cj,dr = map(int,input().split())
    down(0,cj-1,dr,idx)
print(ans)