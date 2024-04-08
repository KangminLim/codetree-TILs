N,M,K = map(int,input().split())
players = {}

arr = [list(map(int,input().split())) for _ in range(N)]
gun = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] > 0: # 총이면
            gun[i][j].append(arr[i][j])
            arr[i][j] = 0
# player 정보 i, j, dir, power, gun, score
for m in range(1,M+1):
    i,j,dir,power = map(int,input().split())
    players[m] = [i-1,j-1,dir,power,0,0]
    arr[i-1][j-1] = m

di,dj = [-1,0,1,0], [0,1,0,-1]
opp = {0:2, 1:3, 2:0, 3:1}

def loser(num,ci,cj,cd,cp,cg,cs):
    for k in range(4):
        ni,nj = ci+di[(cd+k)%4], cj +dj[(cd+k)%4]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj]<=0:
            if gun[ni][nj]:
                cg = max(gun[ni][nj])
            idx = arr[ci][cj]
            arr[ni][nj] = num
            players[num] = [ni,nj,(cd+k)%4,cp,cg,cs]
            return

# M턴 동안 게임 시작
for turn in range(1,K+1):
    # [1] 1~M 플레이어 순서로 한칸 이동
    for idx in range(1,M+1):
        ci,cj,cd,cp,cg,cs = players[idx]
        ni,nj = ci+di[cd],cj+dj[cd]
        # [1-1-1] 범위 밖이면 반대로 이동
        if 0 > ni or ni >= N or 0 > nj or nj >= N:
            cd = opp[cd]
            ni,nj = ci+di[cd],cj+dj[cd]

        arr[ci][cj] = 0

        # [2-1] 이동한 위치에 플레이어가 없는 경우
        if arr[ni][nj] <= 0:
            # [2-1-1] 총이 있는지
            if gun[ni][nj]:
                mx = max(gun[ni][nj]) # 가장 강한 총
                if cg < mx: # 내가 총이 있는지
                    if cg > 0:
                        gun[ni][nj].append(cg)
                    gun[ni][nj].remove(mx)
                    cg = mx
                else: # 내가 총이 없다면
                    gun[ni][nj].remove(mx)
                    cg = mx

            arr[ni][nj] = idx
            players[idx] = [ni, nj, cd, cp, cg, cs]



        # [2-2] 이동한 위치에 적이 있음
        else:
            enemy = arr[ni][nj]
            ei,ej,ed,ep,eg,es = players[enemy]

            # [2-2-1] 플레이어 승리
            if (cg+cp) > (eg+ep) or (cp+cg == eg+ep and cp>ep):
                cs += (cg+cp) - (eg+ep)
                loser(enemy,ei,ej,ed,ep,0,es)

                if cg < eg:
                    if cg > 0:
                        gun[ni][nj].append(cg)
                    cg = eg
                    # arr[ci][cj] = 0
                    arr[ni][nj] = idx
                    players[idx] = [ni, nj, cd, cp, cg, cs]


                else:
                    if eg > 0:
                        gun[ni][nj].append(eg)
                    arr[ni][nj] = idx
                    players[idx] = [ni, nj, cd, cp, cg, cs]

            # [2-2-2] 적 승리
            elif (eg+ep) > (cg+cp) or (cp+cg == eg+ep and ep>cp):
                es += (eg+ep) - (cg+cp)
                loser(idx,ni,nj,cd,cp,0,cs)

                if eg < cg:
                    if eg > 0:
                        gun[ni][nj].append(eg)
                    eg = cg
                    arr[ni][nj] = enemy
                    players[enemy] = [ei, ej, ed, ep, eg, es]


                else:
                    gun[ni][nj].append(cg)
                    arr[ni][nj] = enemy
                    players[enemy] = [ei, ej, ed, ep, eg, es]

for i in range(1,M+1):
    print(players[i][5],end=' ')