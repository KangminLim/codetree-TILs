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
    i,j,dr,power = map(int,input().split())
    players[idx] = [i-1,j-1,dr,power,0,0] # i,j,dr,power,gun,score
    arr[i-1][j-1] = idx

di,dj = [-1,0,1,0], [0,1,0,-1]
opp = {0:2, 1:3, 2:0, 3:1}


def lose(idx,i,j,d,p,g,s):
    for k in range(4):
        ni,nj = i+di[(d+k)%4], j+dj[(d+k)%4]

        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0:
            if gun[ni][nj]:
                g = max(gun[ni][nj])
                gun[ni][nj].remove(g)
            arr[ni][nj] = idx
            players[idx] = [ni,nj,(d+k)%4,p,g,s]
            return

for turn in range(1,K+1):

    for idx in range(1,M+1):
        ci,cj,cd,cp,cg,cs = players[idx]
        ni,nj = ci+di[cd], cj+dj[cd]
        if not (0<=ni<N and 0<=nj<N):
            cd = opp[cd]
            ni,nj = ci+di[cd], cj+dj[cd]

        arr[ci][cj] = 0

        if arr[ni][nj] == 0: # 빈칸이면 총 확인
            if gun[ni][nj]: # 총이 있으면
                mx = max(gun[ni][nj])
                if mx > cg:
                    if cg > 0: # 내가 총이 있으면
                        gun[ni][nj].append(cg)
                    gun[ni][nj].remove(mx)
                    cg = mx

                players[idx] = [ni,nj,cd,cp,cg,cs]
                arr[ni][nj] = idx
            else:
                players[idx] = [ni, nj, cd, cp, cg, cs]
                arr[ni][nj] = idx

        else:
            e = arr[ni][nj]
            ei,ej,ed,ep,eg,es = players[e]

            if cp+cg > ep+eg or (cp+cg==ep+eg and cp>ep):
                cs += ((cp+cg)-(ep+eg))

                if eg > cg: # 적이 내 총보다 쌤
                    if cg > 0: # 난 총을 가지고 있음
                        gun[ni][nj].append(cg)
                    cg = eg
                    players[idx] = [ni, nj, cd, cp, cg, cs]
                    arr[ni][nj] = idx
                else:
                    gun[ni][nj].append(eg)
                    players[idx] = [ni, nj, cd, cp, cg, cs]
                    arr[ni][nj] = idx

                lose(e,ei,ej,ed,ep,0,es)

            else:
                es += ((ep + eg) - (cp + cg))

                if cg > eg:  # 적이 내 총보다 쌤
                    if eg > 0:  # 난 총을 가지고 있음
                        gun[ni][nj].append(eg)
                    eg = cg
                    players[e] = [ni, nj, ed, ep, eg, es]
                    arr[ni][nj] = e
                else:
                    gun[ni][nj].append(cg)
                    players[e] = [ni, nj, ed, ep, eg, es]
                    arr[ni][nj] = e

                lose(idx, ni, nj, cd, cp, 0, cs)

for idx in range(1,M+1):
    print(players[idx][5],end=' ')