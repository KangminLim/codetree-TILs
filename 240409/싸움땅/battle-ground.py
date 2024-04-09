N, M, K = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

gun = [[[] for _ in range(N)] for _ in range(N)]

# 총 처리
for i in range(N):
    for j in range(N):
        if arr[i][j] > 0:
            gun[i][j].append(arr[i][j])
            arr[i][j] = 0

players = {}

# players 정보 : i, j, dir, power, gun power, score
for idx in range(1,M+1):
    i,j,dir,power = map(int,input().split())
    players[idx] = [i-1,j-1,dir,power,0,0]
    arr[i-1][j-1] = idx

di, dj = [-1,0,1,0], [0,1,0,-1]
opp = {0:2,1:3,2:0,3:1}

def lose(idx,ci,cj,cd,cp,cg,cs):

    for k in range(4):
        ni,nj = ci+di[(cd+k)%4], cj+dj[(cd+k)%4]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0:
            if gun[ni][nj]:
                cg = max(gun[ni][nj])
                gun[ni][nj].remove(cg)
            arr[ni][nj] = idx
            players[idx] = [ni,nj,(cd+k)%4,cp,cg,cs] # 플레이어 정보 갱신
            return

# K라운드 동안 게임 진행

for turn in range(1,K+1):

    # [1-1] 1~M번 플레이어부터 순차적으로 본인의 방향대로 이동 (격자를 벗어나는 경우 정반대 방향으로 바꾸어서 이동)
    for idx in players:
        ci,cj,cd,cp,cg,cs = players[idx]
        ni,nj = ci+di[cd], cj+dj[cd]
        # 격자를 벗어나는 경우
        if not (0<=ni<N and 0<=nj<N):
            cd = opp[cd]
            ni,nj = ci+di[cd], cj+dj[cd]
        # 플레이어 이동처리 (이전 위치 = 0)
        arr[ci][cj] = 0

        # [2-1] 만약 이동한 방향에 플레이어가 없다면
        if arr[ni][nj] == 0:
            # [2-1-1] 총이 있는지 확인
            if gun[ni][nj]:
                mx = max(gun[ni][nj]) # 가장 센 총
                # 총을 획득
                if cg < mx: # 가장 센 총 보다 내 총이 약하고
                    if cg > 0: # 내가 총을 가지고 있으면 총 내려두고
                        gun[ni][nj].append(cg)
                    gun[ni][nj].remove(mx)
                    cg = mx
            arr[ni][nj] = idx # 이동 처리
            players[idx] = [ni,nj,cd,cp,cg,cs] # 플레이어 정보 갱신

        # [2-2] 플레이어가 있다면
        else:
            enemy = arr[ni][nj] # 상대방 번호
            ei,ej,ed,ep,eg,es = players[enemy]

            # [2-2-1] 전투 (플레이어 승)
            if (cp+cg) > (ep+eg) or (cp+cg == ep+eg and cp > ep):
                cs += (cp+cg) - (ep+eg)
                lose(enemy,ei,ej,ed,ep,0,es) # 총을 내려두므로 0 처리

                if cg < eg: # 상대방 총이 내 총보다 강함
                    if cg > 0: # 내가 총을 가지고 있을 경우
                        gun[ni][nj].append(cg)
                    cg = eg
                else: # 내 총이 더 강한 경우
                    gun[ni][nj].append(eg)

                arr[ni][nj] = idx # 이동 처리
                players[idx] = [ni,nj,cd,cp,cg,cs] # 플레이어 정보 갱신

            # [2-2-2] 전투 (적 승)
            else:
                es += (ep+eg) - (cp+cg)
                lose(idx,ei,ej,cd,cp,0,cs)

                if eg < cg:
                    if eg > 0:
                        gun[ni][nj].append(eg)
                    eg = cg
                else:
                    gun[ni][nj].append(cg)

                players[enemy] = [ei,ej,ed,ep,eg,es]

for i in players:
    print(players[i][5], end=' ')