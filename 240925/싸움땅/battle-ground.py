N, M, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
gun = [[[] for _ in range(N)] for _ in range(N)]

players = {}
for i in range(N):
    for j in range(N):
        if arr[i][j] > 0:
            gun[i][j].append(arr[i][j])
            arr[i][j] = 0

for idx in range(1,M+1):
    si,sj,dr,power = map(int,input().split())
    # si,sj,dr,power,gun,score
    players[idx] = [si-1,sj-1,dr,power,0,0]
    arr[si-1][sj-1] = idx

di,dj = [-1,0,1,0], [0,1,0,-1]
opp = {0:2,1:3,2:0,3:1}

def lose(cur,ci,cj,cd,cp,cg,cs):
    for k in range(4):
        ni,nj = ci+di[(cd+k)%4],cj+dj[(cd+k)%4]
        if 0<=ni<N and 0<=nj<N and not arr[ni][nj]:
            if gun[ni][nj]:
                cg = max(gun[ni][nj])
                gun[ni][nj].remove(cg)
            players[cur] = [ni,nj,(cd+k)%4,cp,cg,cs]
            arr[ni][nj] = cur
            return

for turn in range(1,K+1):
    # 1.1 모든 플레이어 이동
    for idx in players:
        ci,cj,cd,cp,cg,cs = players[idx]
        ni,nj = ci+di[cd], cj+dj[cd]
        if not (0<=ni<N and 0<=nj<N):
            cd = opp[cd]
            ni, nj = ci + di[cd], cj + dj[cd]
        arr[ci][cj] = 0 # 이동처리

        # 2.1 이동 위치 빈칸이면
        if arr[ni][nj] == 0:
            if gun[ni][nj]:
                mg = max(gun[ni][nj])
                if mg > cg:
                    if cg > 0:
                        gun[ni][nj].append(cg)
                    gun[ni][nj].remove(mg)
                    cg = mg
            arr[ni][nj] = idx
            players[idx] = [ni,nj,cd,cp,cg,cs]

        # 2.2 상대가 있다면
        else:
            e = arr[ni][nj]
            ei,ej,ed,ep,eg,es = players[e]

            # 2.2.1 플레이어 승
            if (cp+cg) > (ep+eg) or ((cp+cg) == (ep+eg) and cp > ep):
                cs += (cp+cg) - (ep+eg)
                if eg > cg:
                    if cg > 0:
                        gun[ni][nj].append(cg)
                    cg = eg
                else:
                    gun[ni][nj].append(eg)
                arr[ni][nj] = idx
                players[idx] = [ni,nj,cd,cp,cg,cs]

                lose(e,ei,ej,ed,ep,0,es)
            # 2.2.2 적 승리
            else:
                es += (ep+eg) - (cp+cg)
                if cg > eg:
                    if eg > 0:
                        gun[ni][nj].append(eg)
                    eg = cg
                else:
                    gun[ni][nj].append(cg)
                arr[ei][ej] = e
                players[e] = [ei,ej,ed,ep,eg,es]

                lose(idx,ni,nj,cd,cp,0,cs)

for idx in players:
    print(players[idx][5],end=' ')