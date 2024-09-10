N,M,K = map(int,input().split())
gun = [[[] for _ in range(N)] for _ in range(N)]
arr = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] > 0:
            gun[i][j].append(arr[i][j])
            arr[i][j] = 0

# x,y,d,p,g,s
players = {}
for idx in range(1,M+1):
    ci,cj,d,p = map(int,input().split())
    # ci,cj,dr,power,gun,score
    players[idx] = [ci-1,cj-1,d,p,0,0]
    arr[ci-1][cj-1] = idx


di,dj = [-1,0,1,0],[0,1,0,-1]
opp = {0:2,1:3,2:0,3:1}

def lose(cur,ci,cj,cd,cp,cg,cs):
    for k in range(4):
        ni,nj = (ci+di[(cd+k)%4]), (cj+dj[(cd+k)%4])
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0:
            if gun[ni][nj]:
                cg = max(gun[ni][nj])
                gun[ni][nj].remove(cg)
            players[cur] = [ni,nj,(cd+k)%4,cp,cg,cs]
            arr[ni][nj] = cur
            return


for turn in range(K):
    # 1-1 첫 번쨰 플레이어부터 순차적으로 본인이 향하고 있는 방향대로 한 칸만큼 이동
    for idx in players:
        ci,cj,cd,cp,cg,cs = players[idx]
        ni,nj = ci+di[cd], cj+dj[cd]
        arr[ci][cj] = 0
        # 해당 방향으로 나갈 때 격자를 벗어나는 경우 -> 반대 방향으로 바꾸기
        if not (0<=ni<N and 0<=nj<N):
            cd = opp[cd]
            ni, nj = ci + di[cd], cj + dj[cd]

        # 2-1 이동한 방향에 플레이어가 없다면
        if arr[ni][nj] == 0:
            if gun[ni][nj]:
                tg = max(gun[ni][nj])
                if tg > cg:
                    if cg > 0:
                        gun[ni][nj].append(cg)
                    gun[ni][nj].remove(tg)
                    cg = tg
            arr[ni][nj] = idx
            players[idx] = [ni,nj,cd,cp,cg,cs]
        # 2-2 이동한 방향에 플레이어가 있다면
        else:
            tn = arr[ni][nj]
            ti,tj,td,tp,tg,ts = players[tn]

            # 2-2-1 능력치 비교
            # 2-2-2 플레이어 승리
            if ((cp+cg) > (tp+tg) or ((cp+cg)==(tp+tg) and cp > tp)):
                cs += (cp+cg) - (tp+tg)
                if tg > cg:
                    if cg > 0:
                        gun[ni][nj].append(cg)
                    cg = tg
                else:
                    gun[ni][nj].append(tg)
                arr[ni][nj] = idx
                players[idx] = [ni,nj,cd,cp,cg,cs]
                lose(tn,ti,tj,td,tp,0,ts)
            else:
                ts += (tp+tg) - (cp+cg)
                if cg > tg:
                    if tg > 0:
                        gun[ni][nj].append(tg)
                    tg = cg
                else:
                    gun[ni][nj].append(cg)
                arr[ti][tj] = tn
                players[tn] = [ti,tj,td,tp,tg,ts]
                lose(idx,ni,nj,cd,cp,0,cs)

for idx in players:
    print(players[idx][5],end=' ')