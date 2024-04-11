N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
from collections import deque

def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v[si][sj] = True
    groups[-1].add((si,sj))
    while q:
        ci,cj = q.popleft()
        for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if 0<=ni<N and 0<=nj<N and not v[ni][nj] and arr[ci][cj] == arr[ni][nj]:
                    q.append((ni,nj))
                    groups[-1].add((ni,nj))
                    v[ni][nj] = True

ans = 0
M = N//2
for k in range(4):
    groups = []
    nums = []
    v = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not v[i][j]:
                groups.append(set())
                nums.append(arr[i][j])
                bfs(i,j)

    cnt = len(nums)
    for i in range(0,cnt-1):
        for j in range(i+1,cnt):
            point = (len(groups[i]) + len(groups[j])) * nums[i] * nums[j]
            for ci,cj in groups[i]:
                for ni,nj in ((ci-1,cj),(ci+1,cj),(ci,cj-1),(ci,cj+1)):
                    if (ni,nj) in groups[j]:
                        ans += point

    if k == 3: break

    narr = [x[:] for x in arr]
    for i in range(N):
        narr[M][i] = arr[i][M]
    for j in range(N):
        narr[j][M] = arr[M][N-j-1]
    for si,sj in ((0,0),(M+1,0),(0,M+1),(M+1,M+1)):
        for i in range(M):
            for j in range(M):
                narr[si+i][sj+j] = arr[si+M-j-1][sj+i]
    arr = narr

print(ans)