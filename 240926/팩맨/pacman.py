M,T = map(int,input().split())
pi,pj = map(lambda x:int(x)-1,input().split())
mlst = []
di,dj = [-1,-1,0,1,1,1,0,-1],[0,-1,-1,-1,0,1,1,1]
arr = [[0] * 4 for _ in range(4)]
tdi,tdj = [-1,0,1,0],[0,-1,0,1]
die = [[0] * 4 for _ in range(4)]
for _ in range(M):
    si,sj,dr = map(int,input().split())
    mlst.append((si-1,sj-1,dr-1))
    arr[si-1][sj-1] += 1

for turn in range(1,T+1):
    # 시체 처리
    for i in range(4):
        for j in range(4):
            if die[i][j] < 0 :
                die[i][j] += 1
    # 1. 몬스터 복제 시도
    tlst = [x[:] for x in mlst]
    narr = [x[:] for x in arr]

    # 2. 몬스터 이동
    for i in range(len(mlst)):
        ci,cj,cd = mlst[i]
        for k in range(8):
            ni,nj = ci+di[(cd+k)%8], cj+dj[(cd+k)%8]
            # 범위 내, 몬스터 시체 x, 팩맨 x
            if 0<=ni<4 and 0<=nj<4 and die[ni][nj] >= 0 and (ni,nj) != (pi,pj):
                narr[ni][nj] += 1
                narr[ci][cj] -= 1
                mlst[i] = (ni,nj,(cd+k)%8)
                break
    arr = narr
    # 3. 팩맨 이동 위치 찾기
    mx = 0
    dlst = []

    # 이동 과정 3회 (상,좌,하,우), 이동 과정에서 먹는 몬스터 mx, dr, 값 저장
    tpi,tpj = pi, pj
    for i in range(4):
        fni,fnj = tpi+tdi[i], tpj+tdj[i]
        if 0<=fni<4 and 0<=fnj<4:
            tmp1 = arr[fni][fnj]
            for j in range(4):
                tmp2 = 0
                sni,snj = fni + tdi[j], fnj + tdj[j]
                if 0 <= sni < 4 and 0 <= snj < 4:
                    if (fni, fnj) != (sni, snj) and (fni, fnj) != (tpi, tpj):
                        tmp2 = arr[sni][snj]
                    for k in range(4):
                        tmp3 = 0
                        tni,tnj = sni+tdi[k],snj+tdj[k]
                        if 0 <= tni < 4 and 0 <= tnj < 4:
                            if (tni,tnj) != (sni,snj) and (tni,tnj) != (fni,fnj) and (tni, tnj) != (tpi, tpj):
                                tmp3 = arr[tni][tnj]
                            tmp = tmp1+tmp2+tmp3
                            if tmp > mx:
                                mx = tmp
                                dlst.append((i,j,k))

    # 4. 팩맨 이동
    if mx > 0:
        slst = []
        i,j,k = dlst[-1]
        fni, fnj = tpi + tdi[i], tpj + tdj[i]
        tmp1 = arr[fni][fnj]
        if tmp1 > 0:
            arr[fni][fnj] = 0
            die[fni][fnj] = -3
        sni, snj = fni + tdi[j], fnj + tdj[j]
        tmp2 = arr[sni][snj]

        if tmp2 > 0:
            arr[sni][snj] = 0
            die[sni][snj] = -3
        tni, tnj = sni + tdi[k], snj + tdj[k]
        tmp3 = arr[tni][tnj]
        if tmp3 > 0:
            arr[tni][tnj] = 0
            die[tni][tnj] = -3
        # 팩맨 이동 처리
        pi,pj = tni, tnj
        for mi,mj,md in mlst:
            if (mi,mj) != (fni,fnj) and (mi,mj) != (sni,snj) and (mi,mj) != (tni,tnj):
                slst.append((mi,mj,md))
        mlst = slst
    else:
        tpi,tpj = pi, pj
        for i in range(4):
            fni, fnj = tpi + tdi[i], tpj + tdj[i]
            if 0 <= fni < 4 and 0 <= fnj < 4:
                for j in range(4):
                    sni, snj = fni + tdi[j], fnj + tdj[j]
                    if 0 <= sni < 4 and 0 <= snj < 4:
                        for k in range(4):
                            tni, tnj = sni + tdi[k], snj + tdj[k]
                            if 0 <= tni < 4 and 0 <= tnj < 4:
                                pi, pj = tni, tnj
                                flag = True
                                break
                    if flag:
                        break
            if flag:
                break


    # 5. 몬스터 복제 완성
    for ti,tj,td in tlst:
        arr[ti][tj] += 1
    mlst += tlst

ans = 0
for i in range(4):
    for j in range(4):
        if arr[i][j] > 0:
            ans += arr[i][j]
print(ans)