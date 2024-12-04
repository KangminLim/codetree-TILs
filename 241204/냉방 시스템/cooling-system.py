di,dj = [0,0,-1,0,1], [0,-1,0,1,0]
N,M,K = map(int,input().split())
in_arr = [[0] * (N+2)] + [[0] + list(map(int,input().split())) + [0] for _ in range(N)] + [[0] * (N+2)]

# [0] 벽 만들기 : 이동 방향에 따라서 이동할 수 없는 경우 벽 룩업 테이블 만들기
wall = [[[0] * 5 for _ in range(N+2)] for _ in range(N+2)]
for _ in range(M):
    i,j,t = map(int,input().split())
    if t == 0:
        wall[i][j][2] = wall[i-1][j][4] = 1
    else:
        wall[i][j][1] = wall[i][j-1][3] = 1

mlst = []
hlst = []

for i in range(1,N+1):
    for j in range(1,N+1):
        if 2<=in_arr[i][j]<=5:
            hlst.append((i,j,in_arr[i][j]-1))
        elif in_arr[i][j] == 1:
            mlst.append((i,j))

# 확산 방향 / 좌, 상, 우, 하
dr_dict = {1:((2,1),(1,),(4,1)),2:((1,2),(2,),(3,2)), 3: ((2,3),(3,),(4,3)), 4:((1,4),(4,),(3,4))}
from collections import deque
def bfs(si,sj,dr):
    q = deque()
    v = [[0] * (N+2) for _ in range(N+2)]

    si, sj = si+di[dr], sj+dj[dr]
    q.append((si,sj,dr))
    v[si][sj] = 5
    arr[si][sj] += 5
    while q:
        ci,cj,dr = q.popleft()
        for dirs in dr_dict[dr]:
            si,sj = ci, cj
            if v[ci][cj] == 1: continue

            for dir in dirs:
                ni,nj = si+di[dir], sj+dj[dir]
                if 1<=ni<=N and 1<=nj<=N and wall[si][sj][dir] == 0 and v[ni][nj] == 0:
                    si,sj = ni,nj
                else:
                    break
            else:
                q.append((ni,nj,dr))
                v[ni][nj] = v[ci][cj] - 1
                arr[ni][nj] += v[ni][nj]

arr = [[0] * (N+2) for _ in range(N+2)]

for ans in range(1,101):
    # [1] 모든 온풍기 바람 확산 (모든 경로에 벽이 없는 경우 확산, 누적)
    for si, sj, dr in hlst:
        bfs(si,sj,dr)
    # [2] 온도 조절 : 모든 칸 기준 (인접 4방향, 벽이 없는 경우 온도 차이 / 4)
    nv = [x[:] for x in arr]
    for i in range(1,N+1):
        for j in range(1,N+1):
            for dr in range(1,5):
                if wall[i][j][dr] == 0: # 벽이 없다면
                    ni,nj = i+di[dr], j+dj[dr]
                    if 1<=ni<=N and 1<=nj<=N:
                        val = (arr[i][j] - arr[ni][nj]) // 4
                        if val > 0:
                            nv[i][j] -= val
                            nv[ni][nj] += val

    arr = nv
    # [3] 바깥쪽 온도 1 감소(>0)
    for j in range(1,N+1):
        arr[1][j] = max(0,arr[1][j]-1)
        arr[N][j] = max(0,arr[N][j]-1)
    for i in range(2,N):
        arr[i][1] = max(0,arr[i][1]-1)
        arr[i][N] = max(0,arr[i][N]-1)

    # [4] 조사 위치 온도 측정(>=K인 경우 중단)
    for i,j in mlst:
        if arr[i][j] < K:
            break
    else:
        break

else:
    ans = -1

print(ans)