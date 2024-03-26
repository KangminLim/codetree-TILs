N, M, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

from collections import deque
def bfs(si,sj,team_n):
    q = deque()
    team = []
    q.append((si,sj))
    v[si][sj] = 1
    team.append((si,sj))
    arr[si][sj] = team_n
    while q:
        ci, cj = q.popleft()
        # 네 방향, 범위 내, 미방문, 조건 : 2 또는 출발지 아닌 곳에서 온 3
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0:
                if arr[ni][nj] == 2 or ((ci,cj) !=(si,sj) and arr[ni][nj]==3):
                    q.append((ni,nj))
                    v[ni][nj] = 1
                    team.append((ni,nj))
                    arr[ni][nj] = team_n

    teams[team_n] = team



v = [[0] * N for _ in range(N)]
team_n = 5
teams = {}
for i in range(N):
    for j in range(N):
        if v[i][j] == 0 and arr[i][j] == 1: # 머리 위치인 경우
            bfs(i,j,team_n)
            team_n += 1
# 우 상 좌 하
di = [0,-1,0,1]
dj = [1,0,-1,0]
ans = 0
for k in range(K): # 라운드 0부터 k-1까지 진행
    # [1] 머리 방향으로 한칸씩 이동
    for team in teams.values(): # 팀 별로 리스트를 가져옴
        ei,ej= team.pop() # 꼬리 좌표 삭제
        arr[ei][ej] = 4  # 이동선으로 복원
        si, sj = team[0] # 머리 좌표
        # 인접한 네 방향(범위 내)에서 4인 값으로 진행(추가)
        for ni, nj in ((si-1,sj), (si+1,sj), (si,sj-1),(si,sj+1)):
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 4:
                team.insert(0,(ni,nj)) # 새 머리 좌표
                arr[ni][nj] = arr[si][sj] # arr 새 머리 좌표에 팀번호 표시
                break

    # [2] 라운드 번호에 맞게 (방향, 시작위치) 계산
    dr = (k//N)%4 # 방향 계산
    offset = k%N
    if dr == 0 : # 우측 좌표
        ci,cj = offset, 0
    elif dr == 1:
        ci,cj = N-1, offset
    elif dr == 2:
        ci,cj = N-1-(offset), N-1
    else:
        ci,cj = 0,N-1-(offset)

    # [3] 공을 받은 사람 점수 추가 및 방향 반전
    for _ in range(N): # 최대 N 범위까지 탐색
        if 0<=ci<N and 0<=cj<N and arr[ci][cj] > 4: # 특정 팀이 공 받았음
            team_n = arr[ci][cj]
            # (해당 좌표 인덱스 +1)
            ans += (teams[team_n].index((ci,cj))+1)  ** 2
            teams[team_n] = teams[team_n][::-1]
            break
        ci, cj = di[dr], dj[dr]
print(ans)