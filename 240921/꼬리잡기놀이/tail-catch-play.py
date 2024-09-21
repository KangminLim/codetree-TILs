N, M, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
v = [[False] * N for _ in range(N)]
team_n = 5
teams = {}
ans = 0

di,dj = [0,-1,0,1], [1,0,-1,0]

from collections import deque

def bfs(si,sj):
    q = deque()
    team = deque()
    q.append((si,sj))
    team.append((si,sj))
    arr[si][sj] = team_n
    v[si][sj] = True

    while q:
        ci,cj = q.popleft()
        for ni, nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if 0<=ni<N and 0<=nj<N and not v[ni][nj]:
                if arr[ni][nj] == 2 or ((ni,nj) != (si,sj) and arr[ni][nj] == 3):
                    q.append((ni,nj))
                    team.append((ni,nj))
                    arr[ni][nj] = team_n
                    v[ni][nj] = True

    teams[team_n]= team

for i in range(N):
    for j in range(N):
        if not v[i][j] and arr[i][j] == 1:
            bfs(i,j)
            team_n += 1

for turn in range(K):

    for team in teams.values():
        ei,ej = team.pop()
        arr[ei][ej] = 4
        si,sj = team[0]
        for ni,nj in ((si-1,sj),(si,sj+1),(si+1,sj),(si,sj-1)):
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 4:
                team.appendleft((ni,nj))
                arr[ni][nj] = arr[si][sj]
                break

    dr = (turn//N)%4
    offset = turn % N

    if dr == 0:
        ci,cj = offset,0
    elif dr == 1:
        ci,cj = N-1, offset
    elif dr == 2:
        ci,cj = N-1-offset, N-1
    else:
        ci,cj = 0, N-1-offset

    for _ in range(N):
        if 0<=ci<N and 0<=cj<N and arr[ci][cj] > 4:
            team_n = arr[ci][cj]
            ans += (teams[team_n].index((ci,cj))+1)**2
            teams[team_n].reverse()
            break
        ci,cj = ci+di[dr],cj+dj[dr]
print(ans)