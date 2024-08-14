N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = 0
M = N//2

from collections import deque

def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v[i][j] = True
    groups[-1].add((si,sj))

    while q:
        ci,cj = q.popleft()
        for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if 0 <= ni < N and 0 <= nj < N and not v[ni][nj] and arr[si][sj] == arr[ni][nj]:
                q.append((ni,nj))
                v[ni][nj] = True
                groups[-1].add((ni,nj))


for t in range(4):

    # 1. 그룹 정하기
    groups, nums = [], []
    v = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not v[i][j] and (i,j) not in groups:
                nums.append(arr[i][j])
                groups.append(set())
                bfs(i,j)

    CNT = len(groups)
    # 2. 점수 구하기
    for i in range(0,CNT-1):
        for j in range(i+1,CNT):
            for ci,cj in groups[i]:
                for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
                    if (ni,nj) in groups[j]:
                        ans += (len(groups[i]) + len(groups[j])) * nums[i] * nums[j]
    if t == 3: break

    # 3. 회전
    narr = [x[:] for x in arr]

    # 3.1 십자 반시계
    # 3.1.1 가로
    for i in range(N):
        narr[i][M] = arr[M][N-1-i]
    # 3.1.2 세로
    for j in range(N):
        narr[M][j] = arr[j][M]
    arr = narr
    narr = [x[:] for x in arr]

    for si,sj in ((0,0),(M+1,0),(0,M+1),(M+1,M+1)):
        for i in range(M):
            for j in range(M):
                narr[si+i][sj+j] = arr[si+M-1-j][sj+i]

    arr = narr
print(ans)