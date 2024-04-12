N, M, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
gun = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] > 0:
            gun[i][j].append((arr[i][j]))
            arr[i][j] = 0

players = {}

for idx in range(1,M+1):
    i,j,dr,power = map(int,input().split())
    players[idx] = [i-1,j-1,dr,power,0,0]
    arr[i-1][j-1] = idx

di,dj = [-1,0,1,0], [0,1,0,-1]

def lose(cur, ci, cj, cd,cp,cg,cs):
    for k in range(4):
        ni,nj = ci+di[(cd+k)%4], cj + dj[(cd+k)%4]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0:
            if gun[ni][nj]:
                cg = max(gun[ni][nj])
                gun[ni][nj].remove(cg)
            players[cur] = [ni,nj,(cd+k)%4,cp,cg,cs]
            arr[ni][nj] = cur
            return

for T in range(1,K+1):

    for idx in range(1,M+1):
        ci,cj,cd,cp,cg,cs = players[idx]

        ni,nj = ci+di[cd], cj+dj[cd]

        if not (0<=ni<N and 0<=nj<N):
            nd = (cd+2)%4
            ni,nj = ci+di[nd], cj+dj[nd]
            cd = nd
        arr[ci][cj] = 0

        # 빈 칸이면
        if arr[ni][nj] == 0:
            if gun[ni][nj]:
                mx = max(gun[ni][nj])
                if mx>cg:
                    if cg > 0:
                        gun[ni][nj].append(cg)
                    gun[ni][nj].remove(mx)
                    cg = mx
            arr[ni][nj] = idx
            players[idx] = [ni,nj,cd,cp,cg,cs]

        else:
            enemy = arr[ni][nj]
            ei,ej,ed,ep,eg,es = players[enemy]

            if (cp+cg) > (ep+eg) or ((cp+cg)==(ep+eg) and cp>ep):
                cs += (cp+cg) - (ep+eg)
                lose(enemy,ei,ej,ed,ep,0,es)

                if eg>cg:
                    if cg>0:
                        gun[ni][nj].append(cg)
                    cg = eg

                else:
                    gun[ni][nj].append(eg)

                players[idx] = [ni,nj,cd,cp,cg,cs]
                arr[ni][nj] = idx

            else:
                es += (ep + eg) - (cp + cg)
                lose(idx, ni, nj, cd, cp, 0, cs)

                if cg > eg:
                    if eg > 0:
                        gun[ni][nj].append(eg)
                    eg = cg

                else:
                    gun[ni][nj].append(cg)

                players[enemy] = [ei, ej, ed, ep, eg, es]
                arr[ni][nj] = enemy

for idx in range(1,M+1):
    print(players[idx][5],end=' ')