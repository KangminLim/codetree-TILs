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
        for ni,nj in ((ci-1,cj),(ci+1,cj),(ci,cj-1),(ci,cj+1)):
            if 0<=ni<N and 0<=nj<N and not v[ni][nj] and arr[ci][cj] == arr[ni][nj]:
                q.append((ni,nj))
                groups[-1].add((si,sj))
                v[ni][nj] = True


for k in range(4):
    groups = []
    nums = []
    v = [[False] * N for _ in range(N)]
    # [1] 그룹화 하기 / 방문하지 않았다면
    for i in range(N):
        for j in range(N):
            if not v[i][j]:
                groups.append(set()) # set으로 중복 제거하면서 추가
                nums.append(arr[i][j]) # 그룹을 이루고 있는 숫자 추가
                bfs(i,j)


    # [2] 예술 점수 구하기
    CNT = len(nums)

    for i in range(0,CNT-1):
        for j in range(1,CNT):
            points = (len(groups[i]) + len(groups[j])) * nums[i] * nums[j]
            for ci, cj in groups[i]:
                for ni,nj in ((ci-1,cj),(ci+1,cj),(ci,cj-1),(ci,cj+1)):
                    if (ni,nj) in groups[j]:
                        ans += points

    # 3회전 예술 점수 구하면 종료
    if k == 3:
        break

    # [3] '+' 반시계 , 4개 사각형 시계방향 회전

    narr = [x[:] for x in arr]

    for i in range(N):
        narr[M][i] = arr[i][M]
    for j in range(N):
        narr[j][M] = arr[M][N-j-1]

    for si,sj in ((0,0),(0,M+1),(M+1,0),(M+1,M+1)):
        for i in range(M):
            for j in range(M):
                narr[si+i][sj+j] = arr[si+N-j-1][sj+i]

    arr = narr

print(ans)