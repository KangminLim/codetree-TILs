N, M, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
gun = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] > 0:
            gun[i][j].append((arr[i][j]))
            arr[i][j] = 0

players = {}

# i,j,dir,power,gun,score
for idx in range(1,M+1):
    x,y,d,s = map(int,input().split())
    players[idx] = [x-1,y-1,d,s,0,0]
    arr[x-1][y-1] = idx

di, dj = [-1,0,1,0], [0,1,0,-1]
opp = {0:2,1:3,2:0,3:1}

def lose(cur,ci,cj,cd,cp,cg,cs):

    for k in range(4):
        ni,nj = ci+di[(cd+k)%4], cj+dj[(cd+k)%4]

        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0:
            if gun[ni][nj]:
                cg = max(gun[ni][nj])
                gun[ni][nj].remove(cg)
            arr[ni][nj] = cur
            players[cur] = [ni,nj,(cd+k)%4,cp,cg,cs]
            return

for turn in range(1,K+1):
    # [1-1]
    for idx in players:
        ci,cj,cd,cp,cg,cs = players[idx]
        ni,nj = ci+di[cd], cj+dj[cd]
        if not (0<=ni<N and 0<=nj<N):
            cd = opp[cd]
            ni,nj = ci+di[cd], cj+dj[cd]

        arr[ci][cj] = 0 # 이동처리

        if arr[ni][nj] == 0: # 빈칸이면
            if gun[ni][nj]: # 총이 있나?
                mx = max(gun[ni][nj])
                if mx > cg:
                    if cg > 0:
                        gun[ni][nj].append(cg)
                    gun[ni][nj].remove(mx)
                    cg = mx
            arr[ni][nj] = idx
            players[idx] = [ni,nj,cd,cp,cg,cs]


        else:
            enemy = arr[ni][nj]
            ei,ej,ed,ep,eg,es = players[enemy]
            # 플레이어 승리
            if (cp+cg) > (ep+eg) or ((cp+cg)==(ep+eg) and cp>ep):
                cs += (cp+cg) - (ep+eg)
                lose(enemy,ei,ej,ed,ep,0,es)

                if cg < eg:
                    if cg > 0:
                        gun[ni][nj].append(cg)
                    cg = eg
                else:
                    gun[ni][nj].append(eg)

                arr[ni][nj] = idx
                players[idx] = [ni,nj,cd,cp,cg,cs]

            # 적 승리
            else:
                es += (ep+eg) - (cp+cg)
                lose(idx, ni,nj,cd,cp,0,cs)

                if eg < cg:
                    if eg > 0:
                        gun[ni][nj].append(eg)
                    eg = cg
                else:
                    gun[ni][nj].append(cg)

                arr[ni][nj] = enemy
                players[enemy] = [ei,ej,ed,ep,eg,es]

for i in players:
    print(players[i][5], end =' ')