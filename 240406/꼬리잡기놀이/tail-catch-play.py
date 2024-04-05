N,M,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
team_n = 5
teams = {}
v = [[False] * N for _ in range(N)]
ans = 0
# 우 상 좌 하
di, dj = [0,-1,0,1], [1,0,-1,0]
from collections import deque

def bfs(si,sj,team_n):
    q = deque()
    team = deque()
    q.append((si,sj))
    team.append((si,sj))
    v[si][sj] = True
    arr[si][sj] = team_n

    while q:
        ci,cj = q.popleft()
        for ni,nj in ((ci-1,cj),(ci+1,cj),(ci,cj-1),(ci,cj+1)):
            if 0<=ni<N and 0<=nj<N and not v[ni][nj]: # 네 방향, 범위 내, 미방문
                if arr[ni][nj] == 2 or ((ci,cj) != (si,sj) and arr[ni][nj] == 3):
                    q.append((ni,nj))
                    team.append((ni,nj))
                    v[ni][nj] = True
                    arr[ni][nj] = team_n
    teams[team_n] = team

for i in range(N):
    for j in range(N):
        if not v[i][j] and arr[i][j] == 1: #미방문 했고 머리이면
            bfs(i,j,team_n)
            team_n += 1

# K턴 동안 진행
for k in range(K):
    # [1] 각 팀은 머리 사람을 따라서 한 칸 이동
    for team in teams.values():
        ei,ej = team.pop() # 꼬리부터 제거
        arr[ei][ej] = 4
        si,sj = team[0]
        for ni,nj in ((si-1,sj),(si+1,sj),(si,sj-1),(si,sj+1)):
            if 0<=ni<N and 0<=nj<=N and arr[ni][nj] == 4:
                team.appendleft((ni,nj))
                arr[ni][nj] = arr[si][sj]
                break

    # [2] 방향 정하기
    dr = (k//N)%4
    offset = k%N

    if dr == 0:
        ci, cj = offset, 0
    elif dr == 1:
        ci, cj = N-1, offset
    elif dr == 2:
        ci, cj = N-1-offset, N-1
    else:
        ci, cj = 0, N-1-offset

    # [3] 공이 던져지는 경우에 해당 선에 사람이 있으면 최초에 만나게되는 사람만이 점수를 얻는다
    for _ in range(N):
        if 0<=ci<N and 0<=cj<N and arr[ci][cj] > 4:
            team_n = arr[ci][cj]
            ans += (teams[team_n].index((ci,cj))+1)**2
            teams[team_n].reverse()
            break
        ci,cj = ci+di[dr], cj + dj[dr]

print(ans)