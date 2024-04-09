N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
M = N//2
from collections import deque

def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v[si][sj] = True
    groups[-1].add((si,sj))
    while q:
        ci,cj = q.popleft()
        for ni,nj in ((ci-1,cj),(ci+1,cj),(ci,cj-1),(ci,cj+1)):
            if 0<=ni<N and 0<=nj<N and not v[ni][nj] and arr[ci][cj] == arr[ni][nj]:
                v[ni][nj] = True
                groups[-1].add((ni,nj))
                q.append((ni,nj))

ans = 0


for k in range(4):
    # [1] 그룹화
    groups = []
    nums = []
    v = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not v[i][j]:
                groups.append((set()))
                nums.append(arr[i][j])
                bfs(i,j)

    # [2] 조화로움 점수 주기
    CNT = len(nums)
    for i in range(0,CNT-1):
        for j in range(i+1,CNT):
            point = (len(groups[i]) + len(groups[j])) * nums[i] * nums[j]
            for ci, cj in groups[i]:
                for ni,nj in ((ci-1,cj),(ci+1,cj),(ci,cj-1),(ci,cj+1)):
                    if (ni,nj) in groups[j]:
                        ans += point

    if k == 3:
        break

    # [3] 십자 반시계, 사각형 시계
    narr = [x[:] for x in arr]

    # 가로
    for i in range(N):
        narr[M][i] = arr[i][M]
    # 세로
    for j in range(N):
        narr[j][M] = arr[M][N-j-1]

    for si,sj in ((0,0),(M+1,0),(0,M+1),(M+1,M+1)):
        for i in range(M):
            for j in range(M):
                narr[si+i][sj+j] = arr[si+M-j-1][sj+i]
    arr = narr

print(ans)