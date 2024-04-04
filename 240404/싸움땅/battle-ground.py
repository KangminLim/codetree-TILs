N, M, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

gun = [[[] for _ in range(N)]for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] > 0: # 총이라면
            gun[i][j].append(arr[i][j])
            arr[i][j] = 0

# i,j,dir,power,gun,score
players = {}
for m in range(1,M+1):
    i,j,d,s = map(int,input().split())
    players[m] = [i-1,j-1,d,s,0,0]
    arr[i-1][j-1] = m

di, dj = [-1,0,1,0], [0,1,0,-1]
opp = {0:2, 1:3, 2:0, 3:1}

def leave(num,ci,cj,cd,cp,cg,cs):

    for k in range(4):
        ni,nj = ci+di[(cd+k)%4], cj+dj[(cd+k)%4]

        if 0<=ni<N and 0<=nj<N and arr[ni][nj]==0:
            if gun[ni][nj]:
                cg = max(gun[ni][nj])
            arr[ni][nj] = num
            players[num] = [ni,nj,(cd+k)%4,cp,cg,cs]
            return

for T in range(1,K+1):
    # 첫 번째 플레이어부터 순차적으로 이동
    for i in players:
        ci,cj,cd,cp,cg,cs = players[i]
        ni,nj = ci+di[cd], cj+dj[cd]
        # [1-1]
        # 범위를 벗어나는 경우
        if 0 > ni or ni >= N or 0 > nj or nj >= N:
            cd = opp[cd]
            ni,nj = ci+di[cd], cj+dj[cd]

        arr[ci][cj] = 0 # 이동을 위해 전 위치 0처리

        # [2-1] 플레이어가 없다면
        if arr[ni][nj] == 0:
            if gun[ni][nj]: # 총이 있다면
                if cg > 0: # 플레이어가 총을 가지고 있다면
                    mx = max(gun[ni][nj])
                    if cg < mx:
                        gun[ni][nj].append(cg) # 내 총은 내려두기
                    gun[ni][nj].remove(mx) # 총기함에서 제거
                    cg = mx # 총 획득
            arr[ni][nj] = i # 이동 처리
            players[i] = [ni,nj,cd,cp,cg,cs] # 플레이어 정보 갱신
        # [2-2-1] 플레이어가 있다면 : 전투
        else:
            enemy = arr[ni][nj]
            ei,ej,ed,ep,eg,es = players[enemy]

            # 플레이어가 승리한 경우
            if cp+cg > ep+eg or (cp+cg == ep+eg and cp > ep):
                cs += (cp+cg) - (ep+eg)

                # [2-2-2] 진 플레이어는 본인이 가지고 있는 총을 해당 격자에 내려놓고 이동
                leave(enemy,ni,nj,ed,ep,0,es)

                # [2-2-3] 이긴 플레이어는 승리한 칸에 떨어져 있는 총들과 원래 있던 총 중 가장 공격력이 높은 총 획득 -> 상대 총 획득
                if cg < eg:
                    gun[ni][nj].append(cg)
                    cg = eg
                else:
                    gun[ni][nj].append(eg)

                arr[ni][nj] = i
                players[i] = [ni,nj,cd,cp,cg,cs]

            # 적이 승리할 경우
            else:
                es += (ep+eg) - (cp+cg)

                leave(i,ni,nj,cd,cp,0,cs)

                if eg < cg:
                    gun[ni][nj].append(eg)
                    eg = cg
                else:
                    gun[ni][nj].append(cg)

                arr[ni][nj] = enemy
                players[enemy] = [ei,ej,ed,ep,eg,es]