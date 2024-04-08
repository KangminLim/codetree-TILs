N,M,K = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

gun = [[[] for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] > 0:
            gun[i][j].append(arr[i][j])
            arr[i][j] = 0

players = {}

for m in range(1,M+1):
    i,j,dir,power = map(int,input().split())
    arr[i-1][j-1] = m
    players[m] = [i-1,j-1,dir,power,0,0]

di,dj = [-1,0,1,0], [0,1,0,-1]
opp = {0:2, 1:3, 2:0, 3:1}


def leave(num,ci,cj,cd,cg,cp,cs):
    for k in range(4):
        ni,nj = ci+di[(cd+k)%4], cj+dj[(cd+k)%4]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0:
            if gun[ni][nj]:
                cg = max(gun[ni][nj])
                gun[ni][nj].remove(cg)
            arr[ni][nj] = num
            players[num] = [ni,nj,(cd+k)%4,cg,cp,cs]
            return


for turn in range(1,K+1):
    # [1] 1~P번 플레이어
    for i in range(1,M+1):
        ci,cj,cd,cp,cg,cs = players[i]
        ni,nj = ci+di[cd], cj+dj[cd]

        # 범위 밖이면 반대 방향
        if not (0<=ni<N and 0<=nj<N):
            cd = opp[cd]
            ni, nj = ci + di[cd], cj + dj[cd]

        arr[ci][cj] = 0 # 이동처리

        # 이동한 곳에 플레이어가 없다면
        if arr[ni][nj] == 0:
            if gun[ni][nj]: # 총이 있다면
                mx = max(gun[ni][nj])
                if mx > cg:
                    if cg > 0:
                        gun[ni][nj].append(cg)
                    gun[ni][nj].remove(mx)
                    cg = mx

            arr[ni][nj] = i
            players[i] = [ni,nj,cd,cp,cg,cs]


        else:
            enemy = arr[ni][nj]
            ei,ej,ed,ep,eg,es = players[enemy]

            # 플레이어 승 적 패배
            if (cp+cg) > (ep+eg) or ((cp+cg) == (ep+eg) and cp>ep):
                cs += (cp+cg) - (ep+eg)
                leave(enemy,ei,ej,ed,ep,0,es)

                if cg < eg: # 상대방 총이 더 썌
                    if cg > 0:
                        gun[ni][nj].append(cg)
                    cg = eg

                else: # 내 총이 더 썌
                    if eg >0:
                        gun[ni][nj].append(eg)

                arr[ni][nj] =i
                players[i] = [ni,nj,cd,cp,cg,cs]


            else:
                es += (ep + eg) - (cp + cg)
                leave(i, ni, nj, cd, cp, 0, cs)

                if eg < cg:  # 내 총이 더 썌
                    if eg > 0:
                        gun[ni][nj].append(eg)
                    eg = cg

                else:  # 내 총이 더 썌
                    if cg > 0:
                        gun[ni][nj].append(cg)

                arr[ni][nj] = enemy
                players[enemy] = [ni, nj, ed, ep, eg, es]


for i in players:
    print(players[i][5], end=' ')