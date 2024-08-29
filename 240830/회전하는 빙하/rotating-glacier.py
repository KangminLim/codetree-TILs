N, Q = map(int,input().split())
N = 2**N
arr = [list(map(int,input().split())) for _ in range(N)]
lv = list(map(int,input().split()))

for l in lv:
    narr = [x[:] for x in arr]
    L = 2**l
    for si in range(0,N,L):
        for sj in range(0,N,L):
            hl = L//2
            # 4 -> 1
            for i in range(hl):
                for j in range(hl):
                    narr[si+i][sj+j] = arr[si+i+hl][sj+j]
            # 1 -> 2
            for i in range(hl):
                for j in range(hl):
                    narr[si+i][sj+j+hl] = arr[si+i][sj+j]
            # 2 -> 3
            for i in range(hl):
                for j in range(hl):
                    narr[si+i+hl][sj+j+hl] = arr[si+i][sj+j+hl]
            # 3 -> 4
            for i in range(hl):
                for j in range(hl):
                    narr[si+i+hl][sj+j] = arr[si+i+hl][sj+j+hl]
    arr = narr

    narr = [x[:] for x in arr]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0: continue
            cnt = 0
            for ni,nj in ((i-1,j),(i,j+1),(i+1,j),(i,j-1)):
                if 0<=ni<N and 0<=nj<N and arr[ni][nj] > 0:
                    cnt += 1
            if cnt <= 2:
                narr[i][j] -= 1
    arr = narr

from collections import deque
def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v[si][sj] = True
    cnt = 1
    while q:
        ci, cj = q.popleft()
        for ni, nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if 0<=ni<N and 0<=nj<N and not v[ni][nj] and arr[ni][nj] > 0:
                q.append((ni,nj))
                v[ni][nj] = True
                cnt += 1
    return cnt

ans1 = sum(map(sum,arr))
ans2 = 0
v = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not v[i][j] and arr[i][j]>0:
            tmp = bfs(i,j)
            if tmp > ans2:
                ans2 = tmp
print(ans1)
print(ans2)