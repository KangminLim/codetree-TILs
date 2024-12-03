R, C, K = map(int,input().split())
arr = [[-1] + [0] * C + [-1] for _ in range(R+3)] + [[-1] * (C+2)]

Exit = [[False] * (C + 2) for _ in range(R + 4)]

ans = 0
di,dj = [-1,0,1,0], [0,1,0,-1]

from collections import deque
def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v = [[False] * (C+2) for _ in range(R+4)]
    v[si][sj] = True
    mx = 0
    while q:
        ci,cj = q.popleft()

        for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if arr[ni][nj] > 0 and not v[ni][nj] and (arr[ci][cj] == arr[ni][nj] or (Exit[ci][cj] and (arr[ci][cj] != arr[ni][nj]))):
                q.append((ni,nj))
                v[ni][nj] = True
                mx = max(mx,ni)
    return mx-2

for idx in range(1,K+1):
    ci = 1
    cj, dr = map(int,input().split())

    while True:
        # 1. 남쪽 이동
        if arr[ci+2][cj] == 0 and arr[ci+1][cj-1] == 0 and arr[ci+1][cj+1] == 0:
            ci += 1
        # 2. 서쪽 이동
        elif arr[ci-1][cj-1] == 0 and arr[ci][cj-2] == 0 and arr[ci+1][cj-1] == 0 and arr[ci+1][cj-2] == 0 and arr[ci+2][cj-1] == 0:
            ci += 1
            cj -= 1
            dr = (dr-1) % 4
        # 3. 동쪽 이동
        elif arr[ci-1][cj+1] == 0 and arr[ci][cj+2] == 0 and arr[ci+1][cj+1] == 0 and arr[ci+1][cj+2] == 0 and arr[ci+2][cj+1] == 0:
            ci += 1
            cj += 1
            dr = (dr+1) % 4
        else:
            break

    if ci < 4:
        arr = [[-1] + [0] * C + [-1] for _ in range(R + 3)] + [[-1] * (C + 2)]
        Exit = [[False] * (C+2) for _ in range(R + 4)]
    else:
        for i,j in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1),(ci,cj)):
            arr[i][j] = idx
        Exit[ci+di[dr]][cj+dj[dr]] = True
        tmp = bfs(ci,cj)
        ans += bfs(ci,cj)
        # print('')
print(ans)