N, M = map(int,input().split())
si,sj,ei,ej = map(int,input().split())
rlst = list(map(int,input().split()))

wlst = []
wdict = {}
for i in range(0,len(rlst),2):
    wlst.append((rlst[i],rlst[i+1]))
    wdict[i//2] = (rlst[i],rlst[i+1])
arr = [list(map(int,input().split())) for _ in range(N)] # 0: 도로, 1: 도로 x, 2:메두사, 3: 출구
arr[si][sj] = 2
arr[ei][ej] = 3

mp = [[0] * N for _ in range(N)] # 사람 표시,

for wi,wj in wlst:
    mp[wi][wj] += 1
mp[si][sj] = -1

from collections import deque

# 상 하 좌 우
drdict = {0:((-1,-1),(-1,0),(-1,1)),1: ((1,-1),(1,0),(1,1)), 2:((-1,-1),(0,-1),(1,-1)),3:((-1,1),(0,1),(1,1))}


pdict = {}
def bfs(si,sj,dr):
    dlst = drdict[dr]
    q = deque()
    q.append((si,sj))
    v = [[False] * N for _ in range(N)]
    v[si][sj] = True
    tlst = []
    cnt = 0
    while q:
        ci,cj = q.popleft()
        if mp[ci][cj] > 0:
            cnt += mp[ci][cj]
            tlst.append((ci,cj))
        for di,dj in dlst:
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and not v[ni][nj]:
                q.append((ni,nj))
                v[ni][nj] = True
    v[si][sj] = False
    if tlst:
        # nv = [x[:] for x in v]
        nq = deque()
        for ti, tj in tlst:
            nq.append((ti, tj))
        if dr == 0: # 상
            while nq:
                ti,tj = nq.popleft()
                if tj < sj:
                    for di,dj in ((-1,-1),(-1,0)):
                        ni,nj = ti+di,tj+dj
                        if 0<=ni<N and 0<=nj<N:
                            v[ni][nj] = False
                            nq.append((ni,nj))
                elif tj > sj:
                    for di,dj in ((-1,1),(-1,0)):
                        ni,nj = ti+di,tj+dj
                        if 0<=ni<N and 0<=nj<N:
                            v[ni][nj] = False
                            nq.append((ni,nj))
                else:
                    for di,dj in ((-1,0),):
                        ni,nj = ti+di,tj+dj
                        if 0<=ni<N and 0<=nj<N:
                            v[ni][nj] = False
                            nq.append((ni,nj))
        elif dr == 1: # 하
            while nq:
                ti,tj = nq.popleft()
                if tj < sj:
                    for di,dj in ((1,-1),(1,0)):
                        ni,nj = ti+di,tj+dj
                        if 0<=ni<N and 0<=nj<N:
                            v[ni][nj] = False
                            nq.append((ni,nj))
                elif tj > sj:
                    for di,dj in ((1,1),(1,0)):
                        ni,nj = ti+di,tj+dj
                        if 0<=ni<N and 0<=nj<N:
                            v[ni][nj] = False
                            nq.append((ni,nj))
                else:
                    for di,dj in ((1,0),):
                        ni,nj = ti+di,tj+dj
                        if 0<=ni<N and 0<=nj<N:
                            v[ni][nj] = False
                            nq.append((ni,nj))
        elif dr == 2: # 좌
            while nq:
                ti,tj = nq.popleft()
                if ti < si:
                    for di,dj in ((-1,-1),(0,-1)):
                        ni,nj = ti+di,tj+dj
                        if 0<=ni<N and 0<=nj<N:
                            v[ni][nj] = False
                            nq.append((ni,nj))
                elif ti > si:
                    for di,dj in ((1,-1),(0,-1)):
                        ni,nj = ti+di,tj+dj
                        if 0<=ni<N and 0<=nj<N:
                            v[ni][nj] = False
                            nq.append((ni,nj))
                else:
                    for di,dj in ((0,-1),):
                        ni,nj = ti+di,tj+dj
                        if 0<=ni<N and 0<=nj<N:
                            v[ni][nj] = False
                            nq.append((ni,nj))
        elif dr == 3: # 우
            while nq:
                ti,tj = nq.popleft()
                if ti < si:
                    for di,dj in ((-1,1),(0,1)):
                        ni,nj = ti+di,tj+dj
                        if 0<=ni<N and 0<=nj<N:
                            v[ni][nj] = False
                            nq.append((ni,nj))
                elif ti > si:
                    for di,dj in ((1,1),(0,1)):
                        ni,nj = ti+di,tj+dj
                        if 0<=ni<N and 0<=nj<N:
                            v[ni][nj] = False
                            nq.append((ni,nj))
                else:
                    for di,dj in ((0,1),):
                        ni,nj = ti+di,tj+dj
                        if 0<=ni<N and 0<=nj<N:
                            v[ni][nj] = False
                            nq.append((ni,nj))
        for ti,tj in tlst:
            if not v[ti][tj]:
                cnt -= mp[ti][tj]

    return cnt, v
def find(si,sj):
    q = deque()
    q.append((si,sj))
    v = [[0] * N for _ in range(N)]
    v[si][sj] = (si,sj)
    tlst = [(ei,ej)]
    while q:
        ci,cj = q.popleft()
        if (ci,cj) == (ei,ej):
            while True:
                ci,cj = v[ci][cj]
                if (ci,cj) == (si,sj):
                    tlst = tlst[::-1]
                    return tlst
                tlst.append((ci,cj))

        for ni,nj in ((ci-1,cj),(ci+1,cj),(ci,cj-1),(ci,cj+1)):
            if 0<=ni<N and 0<=nj<N and not v[ni][nj] and arr[ni][nj] != 1:
                q.append((ni,nj))
                v[ni][nj] = (ci,cj)
    return

flag = False
mlst = find(si,sj)
# print('')
if mlst is None: print(-1)
else:
    for turn in range(len(mlst)):
        # 이동거리, 메두사로 인해 돌이 된 전사의 수, 메두사를 공격
        ans1 = ans2 = ans3 = 0
        ni,nj = mlst[turn]
        if (ni,nj) == (ei,ej):
            flag = True
            break
        # 이동 처리
        arr[si][sj] = 0
        arr[ni][nj] = 2

        mp[si][sj] = 0
        # 이동한 곳에 전사가 있다면
        if mp[ni][nj] > 0:
            # ans2 += mp[ni][nj]
            for idx in range(M):
                if idx not in wdict: continue
                ti,tj = wdict[idx]
                if (ni,nj) == (ti,tj):
                    wdict.pop(idx)
        mp[ni][nj] = -1
        si,sj = ni,nj
        if flag:
            break
        mx = 0
        mv = []
        # 2. 메두사의 공격
        for dr in range(4): # 네 방향중 가장 많이 볼 수 있는 방향 정하기 / 상하좌우
            tmp, tv = bfs(si,sj,dr)
            if tmp > mx:
                mx = tmp
                mv = tv

        ans2 += mx
        # print('')
        # nmp = [x[:] for x in mp]
        # 3. 전사의 이동
        for idx in range(M):
            if idx not in wdict: continue
            ci,cj = wdict[idx]
            if mv[ci][cj] : continue
            mn_dist = abs(ci-si) + abs(cj-sj)
            mi,mj,cnt = 0,0,0
            tlst = []
            # 1번째 이동
            for ni,nj in ((ci-1,cj),(ci+1,cj),(ci,cj-1),(ci,cj+1)): # 상하좌우
                if 0<=ni<N and 0<=nj<N and not mv[ni][nj] and mn_dist > abs(ni-si)+abs(nj-sj):
                    mn_dist = abs(ni-si) + abs(nj-sj)
                    tlst.append((ni,nj,1))
                    # 2번쨰 이동
                    for nni, nnj in ((ni,nj-1),(ni,nj+1),(ni-1,nj),(ni+1,nj)): #좌우상하
                        if 0 <= nni < N and 0 <= nnj < N and not mv[nni][nnj] and mn_dist > abs(nni - si) + abs(nnj - sj):
                            mn_dist = abs(nni - si) + abs(nnj - sj)
                            tlst.append((nni, nnj,2))
            if tlst:
                ti,tj,cnt = tlst[-1]
                ans1 += cnt
                if (ti,tj) == (si,sj):
                    ans3 += 1
                    wdict.pop(idx)
                    mp[ci][cj] -= 1
                else:
                    mp[ci][cj] -= 1
                    mp[ti][tj] += 1
                    wdict[idx] = (ti,tj)
        # print('')
        # mp = nmp
        print(ans1,ans2,ans3)
if flag:
    print(0)