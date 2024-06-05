from collections import deque
R,C,K = map(int,input().split())
di,dj = [-1,0,1,0], [0,1,0,-1]
ans = 0

arr = [[0] * C for _ in range(R+3)]
Exit = [[False] * C for _ in range(R+3)]

def isrange(i,j):
    return 3<=i<R+3 and 0<=j<C

def bfs(i,j):
    q = deque()
    q.append((i,j))
    v = [[False] * C for _ in range(R+3)]
    v[i][j] = True
    result = i
    while q:
        ci,cj = q.popleft()

        for ni, nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if isrange(ni,nj) and not v[ni][nj] and (arr[ci][cj] == arr[ni][nj] or (arr[ni][nj] != 0 and Exit[ci][cj])):
                q.append((ni,nj))
                v[ni][nj] = True
                result = max(result,ni)
    return result

def cango(i,j):
    flag = 0 <= j-1 and j+1 < C and i+1 < R+3
    flag = flag and (arr[i-1][j-1]==0)
    flag = flag and (arr[i - 1][j] == 0)
    flag = flag and (arr[i - 1][j + 1] == 0)
    flag = flag and (arr[i][j - 1] == 0)
    flag = flag and (arr[i][j] == 0)
    flag = flag and (arr[i][j + 1] == 0)
    flag = flag and (arr[i + 1][j] == 0)
    return flag

def down(i,j,d,id):
    if cango(i+1,j):
        down(i+1,j,d,id)
    elif cango(i+1,j-1):
        down(i+1,j-1,(d+3)%4,id)
    elif cango(i+1,j+1):
        down(i+1,j+1,(d+1)%4,id)
    else: # 1,2,3 모두 안될 경우
        if not isrange(i-1,j-1) or not isrange(i+1,j+1): # 골렘의 몸 일부가 숲을 벗어난 상태
            for i in range(R+3):
                for j in range(C):
                    arr[i][j] = 0
                    Exit[i][j] = False

        else:
            arr[i][j] = id
            for k in range(4):
                arr[i+di[k]][j+dj[k]] = id
            Exit[i+di[d]][j+dj[d]] = True
            global ans
            ans += bfs(i,j) - 3 + 1


for id in range(1,K+1):
    cj, d = map(int,input().split())
    down(0,cj-1,d,id)
print(ans)