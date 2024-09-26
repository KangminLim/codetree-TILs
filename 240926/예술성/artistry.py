N = int(input())
M = N//2

arr = [list(map(int,input().split())) for _ in range(N)]
ans = 0
from collections import deque
# 2. 그룹 정하기 bfs 함수
def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v[si][sj] = True
    # groups[-1].append((si,sj))
    groups[-1].add((si,sj))
    while q:
        ci,cj = q.popleft()
        for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if 0<=ni<N and 0<=nj<N and not v[ni][nj] and arr[ci][cj] == arr[ni][nj]:
                q.append((ni,nj))
                v[ni][nj] = True
                # groups[-1].append((ni,nj))
                groups[-1].add((ni,nj))


for t in range(4):
    v = [[False] * N for _ in range(N)]
    groups = []
    nums = []
    #  1. 그룹 정하기
    for i in range(N):
        for j in range(N):
            if not v[i][j]:
                groups.append(set())
                nums.append(arr[i][j])
                bfs(i,j)
    # 3. 예술성 점수 구하기
    for i in range(len(groups)-1):
        for j in range(i+1,len(groups)):
            for ci,cj in groups[i]:
                for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
                    if (ni,nj) in groups[j]:
                        ans += (len(groups[i])+len(groups[j])) * nums[i] * nums[j]

    # 종료 조건
    if t == 3:
        break

    # 4. 회전
    narr = [x[:] for x in arr]

    # 4.1 십자가 반시계
    for i in range(N):
        narr[i][M] = arr[M][N-1-i]
    for j in range(N):
        narr[M][j] = arr[j][M]

    # 4.2 4방향 시계 회전
    for si,sj in ((0,0),(0,M+1),(M+1,0),(M+1,M+1)):
        for i in range(M):
            for j in range(M):
                narr[si+i][sj+j] = arr[si+M-j-1][sj+i]

    arr = narr

print(ans)