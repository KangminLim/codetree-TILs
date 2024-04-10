N, M, K = map(int,input().split())
team_n = 5
teams = {}
ans = 0
arr = [list(map(int,input().split())) for _ in range(N)]

di,dj = [0,-1,0,1], [1,0,-1,0]
v = [[False] * N for _ in range(N)]

from collections import deque

def bfs(si,sj,team_n):
    q = deque()
    q.append((si,sj))
    team = deque()
    team.append((si,sj))
    arr[si][sj] = team_n

    while q:
        ci, cj = q.popleft()
        for ni, nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if 0<=ni<N and 0<=nj<N and not v[ni][nj]:
                if arr[ni][nj] == 2 or ((ci,cj) != (si,sj) and arr[ni][nj] ==3):
                    v[ni][nj] = True
                    q.append((ni,nj))
                    team.append((ni,nj))
                    arr[ni][nj] = team_n
    teams[team_n] = team

# 그룹화
for i in range(N):
    for j in range(N):
        if not v[i][j] and arr[i][j] == 1:
            bfs(i,j,team_n)
            team_n += 1

# k턴 동안 진행
for k in range(K):
    for team in teams.values():
        ei,ej = team.pop()
        arr[ei][ej] = 4 #꼬리부터 처리
        si,sj = team[0]
        for ni,nj in ((si-1,sj),(si,sj+1),(si+1,sj),(si,sj-1)):
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] ==4:
                team.appendleft((ni,nj))
                arr[ni][nj] = arr[si][sj]
                break


    # 화살표 방향
    dr = (k//N)%4
    offset = k%N

    if dr == 0:
        ci,cj = offset,0
    elif dr == 1:
        ci,cj = N-1,offset
    elif dr == 2:
        ci,cj = N-1-offset, N-1
    else:
        ci,cj = 0, N-1-offset

    for _ in range(N):
        if 0<=ni<N and 0<=nj<N and arr[ci][cj] > 4:
            team_n = arr[ci][cj]
            ans += (teams[team_n].index((ci,cj))+1)**2
            teams[team_n].reverse()
            break

        ci,cj = ci+di[dr], cj+dj[dr]

print(ans)