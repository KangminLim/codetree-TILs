N,M,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
players = {}
gun = [[[] for _ in range(N)] for _ in range(N)]
di,dj = [-1,0,1,0], [0,1,0,-1]

for i in range(N):
    for j in range(N):
        if arr[i][j] > 0:
            gun[i][j].append(arr[i][j])
            arr[i][j] = 0

for idx in range(1,M+1):
    i,j,dr,power = map(int,input().split())
    players[idx] = [i-1,j-1,dr,power,0,0] # i,j,dr,power,gun,score
    arr[i-1][j-1] = idx

def lose(ci,cj,cd,cp,cg,cs,idx):
    for k in range(4):
        ni,nj = ci+di[(cd+k)%4], cj+dj[(cd+k)%4]

        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0:
            if gun[ni][nj]:
                cg = max(gun[ni][nj])
                gun[ni][nj].remove(cg)
            arr[ni][nj] = idx
            players[idx] = [ni,nj,(cd+k)%4,cp,cg,cs]
            return

opp = {0:2,1:3,2:0,3:1}

for turn in range(K):
    # 1-1 첫 번쨰 플레이어부터 본인의 방향대로 이동
    for idx in range(1,M+1):
        ci,cj,cd,cp,cg,cs = players[idx]
        ni,nj = ci+di[cd], cj+dj[cd]
        # 격자 벗어나면 반대방향 이동
        if not (0<=ni<N and 0<=nj<N):
            ni, nj = ci - di[cd], cj - dj[cd]
            cd = opp[cd]
        arr[ci][cj] = 0 # 플레이어 이동처리

        # 2-1 이동한 칸에 플레이어 없다면
        if arr[ni][nj] == 0:
            if cg > 0: # 플레이어가 총을 가지고 있다면
                if gun[ni][nj]:
                    mx = max(gun[ni][nj])
                    if cg < mx: # 내 총이 더 약하면
                        gun[ni][nj].append(cg)
                        cg = mx
                        gun[ni][nj].remove(mx)
                players[idx] = [ni, nj, cd, cp, cg, cs]
                arr[ni][nj] = idx
            else:
                if gun[ni][nj]:
                    cg = max(gun[ni][nj])
                    gun[ni][nj].remove(cg)
                players[idx] = [ni,nj,cd,cp,cg,cs]
                arr[ni][nj] = idx

        # 2-2 플레이어가 있다면
        else:
            e = arr[ni][nj]
            ei,ej,ed,ep,eg,es = players[e] # 상대의 정보
            # 플레이어 승리
            if (cp+cg)>(ep+eg) or (cp+cg==ep+eg and cp > ep):
                cs += (cp+cg)-(ep+eg)
                if cg > 0:
                    if cg < eg:
                        gun[ni][nj].append(cg) # 총 내려두고
                        cg = eg
                    else:
                        gun[ni][nj].append(eg)
                else:
                    cg = eg

                players[idx] = [ni, nj, cd, cp, cg, cs]
                arr[ni][nj] = idx
                lose(ei,ej,ed,ep,0,es,e)

            else:
                es += (ep+eg)-(cp+cg)
                if eg > 0:
                    if eg < cg:
                        gun[ni][nj].append(eg) # 총 내려두고
                        eg = cg
                    else:
                        gun[ni][nj].append(cg)
                else:
                    eg = cg

                players[e] = [ei, ej, ed, ep, eg, es]
                arr[ni][nj] = e
                lose(ni,nj,cd,cp,0,cs,idx)

for i in range(1,M+1):
    ci,cj,cd,cp,cg,cs = players[i]
    print(cs,end=' ')