N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
M = N//2
ans = 0

from collections import deque
def bfs(si,sj,groups,nums,v):
    q = deque()
    q.append((si,sj))
    v[i][j] = True
    groups[-1].add((si,sj))
    while q:
        ci,cj = q.popleft()
        for ni,nj in ((ci-1,cj),(ci+1,cj),(ci,cj-1),(ci,cj+1)):
            if 0<=ni<N and 0<=nj<N and not v[ni][nj] and arr[ci][cj] == arr[ni][nj]:
                q.append((ni,nj))
                groups[-1].add((ni,nj))
                v[ni][nj] = True


for turn in range(4):
    # 1. 그룹 정하기
    nums = []
    groups = []
    v = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not v[i][j] and (i,j) not in groups:
                groups.append(set())
                nums.append(arr[i][j])
                bfs(i,j,groups,nums,v)
    # 2. 예술성 점수 구하기
    CNT = len(groups)
    for i in range(0,CNT-1):
        for j in range(i+1,CNT):
            for ci, cj in groups[i]:
                for ni,nj in ((ci-1,cj),(ci+1,cj),(ci,cj-1),(ci,cj+1)):
                    if 0<=ni<N and 0<=nj<N and (ni,nj) in groups[j]:
                        tmp = (len(groups[i]) + len(groups[j])) * nums[i] * nums[j]
                        ans += tmp
    if turn == 3: break
    # 3. 회전
    narr = [x[:] for x in arr]
    # 3.1 십자 모양 반시계
    for i in range(N):
        narr[i][M] = arr[M][N-1-i]
    for j in range(N):
        narr[M][j] = arr[j][M]

    for si,sj in ((0,0),(M+1,0),(0,M+1),(M+1,M+1)):
        for i in range(M):
            for j in range(M):
                narr[si+i][sj+j] = arr[si+M-1-j][sj+i]
    arr = narr

print(ans)