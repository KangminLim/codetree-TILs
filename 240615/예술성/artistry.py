N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = 0
M = N//2
from collections import deque
def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v[si][sj] = True
    groups[-1].add((si,sj))

    while q:
        ci,cj = q.popleft()
        for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if 0<=ni<N and 0<=nj<N and not v[ni][nj] and arr[si][sj] == arr[ni][nj]:
                q.append((ni,nj))
                groups[-1].add((ni,nj))
                v[ni][nj] = True


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

    CNT = len(groups)

    for i in range(0,CNT-1):
        for j in range(i+1,CNT):
            tmp = (len(groups[i]) + len(groups[j])) * nums[i] * nums[j]
            for ci,cj in groups[i]:
                for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
                    if 0<=ni<N and 0<=nj<N and (ni,nj) in groups[j]:
                        ans += tmp


    if k == 3: break

    narr = [x[:] for x in arr]

    for i in range(N): # 십자 세로
        narr[i][M] = arr[M][N-1-i]

    for j in range(N): # 십자 가로
        narr[M][j] = arr[j][M]

    for si,sj in ((0,0),(M+1,0),(0,M+1),(M+1,M+1)):
        for i in range(M):
            for j in range(M):
                narr[si+i][sj+j] = arr[si+M-1-j][sj+i]
    arr = narr
print(ans)