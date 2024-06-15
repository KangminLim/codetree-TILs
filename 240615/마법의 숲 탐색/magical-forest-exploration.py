R,C,K = map(int,input().split())
ans = 0
arr = [[0] * C for _ in range(R+3)]
Exit = [[False] * C for _ in range(R+3)]
di,dj = [-1,0,1,0],[0,1,0,-1]

from collections import deque
def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v = [[False] * C for _ in range(R+3)]
    v[si][sj] = True
    result = si
    while q:
        ci,cj = q.popleft()
        for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if inrange(ni,nj) and not v[ni][nj] and ((arr[ni][nj] == arr[ci][cj]) or (arr[ni][nj] != 0 and Exit[ci][cj])):
                q.append((ni,nj))
                v[ni][nj] = True
                result = max(result,ni)

    return result
def check(i,j):
    flag = 0<=j-1 and j+1<C and i+1 < R+3
    flag = flag and arr[i-1][j-1] == 0 and arr[i-1][j] == 0 and arr[i-1][j+1] == 0
    flag = flag and arr[i][j-1] == 0 and arr[i][j] == 0 and arr[i][j+1] == 0 and arr[i+1][j] == 0
    return flag


def inrange(i,j):
    return 3<=i<R+3 and 0<=j<C

def down(i,j,dr,idx):
    if check(i+1,j):
        down(i+1,j,dr,idx)
    elif check(i+1,j-1):
        down(i+1,j-1,(dr+3)%4,idx)
    elif check(i+1,j+1):
        down(i+1,j+1,(dr+1)%4,idx)
    else:
        if not inrange(i-1,j-1) or not inrange(i+1,j+1):
            for i in range(R+3):
                for j in range(C):
                    arr[i][j] = 0
                    Exit[i][j] = False
        else:
            arr[i][j] = idx
            for k in range(4):
                arr[i+di[k]][j+dj[k]] = idx
            Exit[i+di[dr]][j+dj[dr]] = True

            global ans
            ans += bfs(i,j) - 3 + 1



for idx in range(1,K+1):
    cj, dr = map(int,input().split())
    down(0,cj-1,dr,idx)
print(ans)