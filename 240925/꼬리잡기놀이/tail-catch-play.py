N, M, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
team_n = 5

from collections import deque

teams = {}

# 1. bfs 함수 (그룹화를 위한)
def bfs(si,sj,v,team_n):
    q = deque()
    q.append((si,sj))
    v[si][sj] = True
    arr[si][sj] = team_n
    team = deque()
    team.append((si,j))
    while q:
        ci,cj = q.popleft()
        for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if 0<=ni<N and 0<=nj<N and not v[ni][nj] and (arr[ni][nj]==2 or (arr[ni][nj] == 3) and (si,sj) != (ci,cj)):
                q.append((ni,nj))
                team.append((ni,nj))
                v[ni][nj] = True
                arr[ni][nj] = team_n

    teams[team_n] = team

di,dj = [0,-1,0,1], [1,0,-1,0]
ans = 0

# 0. 팀 설정
v = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            bfs(i,j,v,team_n)
            team_n += 1

for k in range(K):
    # 2. 머리 이동
    for team in teams.values():
        si,sj = team[0]
        ei,ej = team.pop()
        arr[ei][ej] = 4
        for ni,nj in ((si-1,sj),(si,sj+1),(si+1,sj),(si,sj-1)):
            if 0 <= ni < N and 0<=nj<N and arr[ni][nj] == 4:
                arr[ni][nj] = arr[si][sj]
                team.appendleft((ni,nj))
                break
    # 3. 공 던지기
    dr = (k//N)%4
    offset = k%N

    if dr == 0:
        ci,cj = offset, 0
    elif dr == 1:
        ci,cj = N-1, offset
    elif dr == 2:
        ci,cj = N-1-offset, N-1
    else:
        ci,cj = 0, N-1-offset
    # 4. 점수 획득
    for _ in range(N):
        if arr[ci][cj] > 4:
            tmp = arr[ci][cj]
            ans += (teams[tmp].index((ci,cj))+1)**2
            teams[tmp].reverse()
            break
        else:
            ci,cj = ci+di[dr], cj+dj[dr]
print(ans)