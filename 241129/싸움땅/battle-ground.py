N, M, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
gun = [[[] for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] > 0:
            gun[i][j].append(arr[i][j])
            arr[i][j] = 0

players = {}

for idx in range(1,M+1):
    ci,cj,cd,cs = map(int,input().split())
    players[idx] = [ci-1,cj-1,cd,cs,0,0]
    arr[ci-1][cj-1] = idx

di,dj = [-1,0,1,0],[0,1,0,-1]
opp = {0:2,1:3,2:0,3:1}

def lose(num,ci,cj,cd,cp,cg,cs):
    for k in range(4):
        ni,nj = ci+di[(cd+k)%4], cj + dj[(cd+k)%4]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0:
            if gun[ni][nj]:
                cg = max(gun[ni][nj])
                gun[ni][nj].remove(cg)
            arr[ni][nj] = num
            players[num] = [ni,nj,(cd+k)%4,cp,cg,cs]
            return

for turn in range(1,K+1):
    # 1-1 1번 플레이어부터 이동, 격자 벗어나면 반대 방향 이동
    for idx in players:
        ci,cj,cd,cp,cg,cs = players[idx]
        ni,nj = ci+di[cd],cj+dj[cd]
        if not (0<=ni<N and 0<=nj<N):
            cd = opp[cd]
            ni, nj = ci + di[cd], cj + dj[cd]
        # 이동 처리
        arr[ci][cj] = 0

        # 2-1 플레이어가 없다면
        if arr[ni][nj] == 0:
            if gun[ni][nj]:
                tg = max(gun[ni][nj])
                if tg > cg:
                    if cg > 0:
                        gun[ni][nj].append(cg)
                    gun[ni][nj].remove(tg)
                    cg = tg
            # 이동 처리
            players[idx] = [ni,nj,cd,cp,cg,cs]
            arr[ni][nj] = idx

        # 2-2 적이 있다면
        else:
            e = arr[ni][nj]
            ei,ej,ed,ep,eg,es = players[e]

            # 2-2-1 플레이어 승리
            if (cp+cg) > (ep+eg) or ((cp+cg) == (ep+eg) and cp > ep):
                cs += (cp+cg) - (ep+eg)
                if eg > cg:
                    if cg > 0:
                        gun[ni][nj].append(cg)
                    cg = eg
                else:
                    gun[ni][nj].append(eg)
                players[idx] = [ni,nj,cd,cp,cg,cs]
                arr[ni][nj] = idx
                lose(e,ei,ej,ed,ep,0,es)
            # 2-2-2 적 승리
            else:
                es += (ep+eg) - (cp+cg)
                if cg > eg:
                    if eg > 0:
                        gun[ni][nj].append(eg)
                    eg = cg
                else:
                    gun[ni][nj].append(cg)
                players[e] = [ni,nj,ed,ep,eg,es]
                arr[ni][nj] = e
                lose(idx,ni,nj,cd,cp,0,cs)

for idx in players:
    print(players[idx][5],end=' ')