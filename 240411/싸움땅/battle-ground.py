N,M,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
gun = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] > 0:
            gun[i][j].append(arr[i][j])
            arr[i][j] = 0

players = {}

# 플레이어들의 정보를 모두 저장 -> i,j,dr,power,gun,score
for idx in range(1,M+1):
    i,j,dir,power = map(int,input().split())
    arr[i-1][j-1] = idx
    players[idx] = [i-1,j-1,dir,power,0,0]


di,dj = [-1,0,1,0],[0,1,0,-1]
opp = {0:2,1:3,2:0,3:1}

def lose(cur,ci,cj,cd,cp,cg,cs):

    for k in range(4):
        ni,nj = ci+di[(cd+k)%4], cj+dj[(cd+k)%4]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0:
            if gun[ni][nj]:
                cg = max(gun[ni][nj])
            arr[ni][nj] = cur
            players[cur] = [ni,nj,(cd+k)%4,cp,cg,cs]
            return

for k in range(1,K+1):
    # [1-1] 1~M 번 본인이 향하고 있는 방향으로 이동
    for idx in range(1,M+1):
        ci,cj,cd,cp,cg,cs = players[idx]
        ni,nj = ci+di[cd], cj+dj[cd]
        # 격자를 벗어나면 반대방향
        if not (0<=ni<N and 0<=nj<N):
            cd = opp[cd]
            ni,nj = ci+di[cd], cj+dj[cd]

        arr[ci][cj] = 0 # 이동 처리 (이동 전 자리)

        if arr[ni][nj] == 0 : # 이동한 곳이 빈칸
            if gun[ni][nj]: # 총이 있다면
                mx = max(gun[ni][nj]) # 가장 센 총
                if mx > cg: # 가장 센 총 > 내 총
                    if cg > 0: # 내가 총이 있다면
                        gun[ni][nj].append(cg) # 총 내려두기
                    gun[ni][nj].remove(mx) # 총 줍기
                    cg = mx
            arr[ni][nj] = idx
            players[idx] = [ni,nj,cd,cp,cg,cs]

        else:
            enemy = arr[ni][nj] # 그 자리에 있는 플레이어
            ei,ej,ed,ep,eg,es = players[enemy]

            if (cp+cg) > (ep+eg) or ((cp+cg) == (ep+eg) and cp>ep): # 플레이어가 승리한다면
                cs += (cp+cg) - (ep+eg)
                lose(enemy,ei,ej,ed,ep,0,es)

                if cg < eg: # 상대방 총이 내 총보다 강하면
                    if cg > 0: # 내가 총이 있다면
                        gun[ni][nj].append(cg)
                    cg = eg
                else:
                    gun[ni][nj].append(eg)

                arr[ni][nj] = idx
                players[idx] = [ni,nj,cd,cp,cg,cs]

            else:
                es += (ep+eg) - (cp+cg)
                lose(idx,ni,nj,cd,cp,0,cs)

                if eg < cg:
                    if eg>0:
                        gun[ni][nj].append(eg)
                    eg = cg
                else:
                    gun[ni][nj].append(cg)

                arr[ni][nj] = enemy
                players[enemy] = [ei,ej,ed,ep,eg,es]

for i in range(1,M+1):
    print(players[i][5], end=' ')