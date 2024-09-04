N, M, K = map(int,input().split())
alst = [list(map(int,input().split())) for _ in range(M)]
arr = [[0] * N for _ in range(N)]

for idx in range(M):
    x,y,m,s,d = alst[idx]
    arr[x-1][y-1] += 1
    alst[idx] = [x-1,y-1,m,s,d]

di,dj = [-1,-1,0,1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1]

for turn in range(1,K+1):
    # 1. 모든 원소는 1초 지날 때마다 자신의 방향으로 속력만큼 이동
    narr = [x[:] for x in arr]
    for idx in range(M):
        # x, y, 질량, 속력, 방향
        ci, cj, cm, cs, cd = alst[idx]
        ni, nj = (ci+di[cd]*cs)%N, (cj+dj[cd]*cs)%N
        narr[ci][cj] -= 1
        narr[ni][nj] += 1
        alst[idx] = [ni,nj,cm,cs,cd]
    arr = narr
    alst.sort(key = lambda x:(x[0],x[1]))
    # 새로 생기는 원자 리스트
    talst = []
    # 2. 이동이 모두 끝난 뒤에 하나의 칸에 2개 이상의 원자가 있는 경우
    # 2.a 같은 칸에 있는 원자들은 각각의 질량과 속력을 모두 합한 하나의 원자로 합쳐진다.
    narr = [x[:] for x in arr]
    for i in range(N):
        for j in range(N):
            # 2개 이상의 원자가 있으면
            if arr[i][j] >= 2:
                tlst = []
                cur = arr[i][j]
                # tlst을 통해 2개 이상의 원자 lst 만들기
                for idx in range(len(alst)):
                    ci, cj, cm, cs, cd = alst[idx]
                    if (ci,cj) != (i,j): continue
                    if not tlst:
                        tlst = [[ci, cj, cm, cs, cd]]
                    else:
                        tlst.append([ci, cj, cm, cs, cd])
                if tlst:
                    # 질량, 속력, 방향(모두 상하좌우 or 대각선 체크)
                    tm,ts,td,flag = 0, 0, tlst[0][4]%2, True
                    for idx in range(len(tlst)):
                        ci, cj, cm, cs, cd = tlst[idx]
                        tm += cm
                        ts += cs
                        # 하나라도 다르면 대각선 아니면 상하좌우
                        if td != (cd%2):
                            flag = False
                    tm = int(tm//5)
                    if tm == 0:
                        narr[i][j] = 0
                        continue
                    ts = int(ts//cur)
                    # 상하좌우
                    if flag:
                        for dr in range(0,8,2):
                            talst.append([i,j,tm,ts,dr])
                            narr[i][j] = 4
                    else:
                        for dr in range(1,8,2):
                            talst.append([i,j,tm,ts,dr])
                            narr[i][j] = 4

    alst = talst
    arr = narr

print(sum(map(sum,arr)))