from collections import deque

K, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(5)]
tlst = list(map(int,input().split()))
tq = deque(tlst)
ans = []

def bfs(si,sj,g,v,arr):
    q = deque()
    q.append((si,sj))
    v[si][sj] = True
    g[-1].add((si,sj))
    cnt = 1
    while q:
        ci,cj = q.popleft()
        for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if 0<=ni<5 and 0<=nj<5 and not v[ni][nj] and arr[si][sj] == arr[ni][nj]:
                q.append((ni,nj))
                v[ni][nj] = True
                g[-1].add((ni,nj))
                cnt += 1
    if cnt >= 3: return cnt
    else: return 0

def rot90(si,sj,arr):
    narr = [x[:] for x in arr]

    for i in range(3):
        for j in range(3):
            narr[si+i][sj+j] = arr[si+2-j][sj+i]

    return narr

def rot180(si,sj,arr):
    narr = [x[:] for x in arr]

    for i in range(3):
        for j in range(3):
            narr[si+i][sj+j] = arr[si+2-i][sj+2-j]

    return narr

def rot270(si,sj,arr):
    narr = [x[:] for x in arr]

    for i in range(3):
        for j in range(3):
            narr[si+i][sj+j] = arr[si+j][sj+2-i]

    return narr

def simul90(arr):
    mx = 0
    marr = []
    # (0,0) ~ (2,2)로 시작
    for si in range(3):
        for sj in range(3):
            arr90 = rot90(sj,si,arr)
            v = [[False] * 5 for _ in range(5)]
            g = []
            sm = 0
            for i in range(5):
                for j in range(5):
                    if not v[i][j]:
                        g.append(set())
                        tmp = bfs(i,j,g,v,arr90)
                        if tmp >= 3:
                            sm += tmp
            if sm > mx:
                mx = sm
                marr = arr90
                mg = []
                for tg in g:
                    if len(tg) >= 3:
                        for ti,tj in tg:
                            mg.append((ti,tj))
    if mx > 0:
        return mx, marr, mg
    else:
        return 0,[],[]

def simul180(arr):
    mx = 0
    marr = []
    # (0,0) ~ (2,2)로 시작
    for si in range(3):
        for sj in range(3):
            arr180 = rot180(sj,si,arr)
            v = [[False] * 5 for _ in range(5)]
            g = []
            sm = 0
            for i in range(5):
                for j in range(5):
                    if not v[i][j]:
                        g.append(set())
                        tmp = bfs(i,j,g,v,arr180)
                        if tmp >= 3:
                            sm += tmp
            if sm > mx:
                mx = sm
                marr = arr180
                mg = []
                for tg in g:
                    if len(tg) >= 3:
                        for ti,tj in tg:
                            mg.append((ti,tj))
    if mx > 0:
        return mx, marr, mg
    else:
        return 0,[],[]


def simul270(arr):
    mx = 0
    marr = []
    # (0,0) ~ (2,2)로 시작
    for si in range(3):
        for sj in range(3):
            arr270 = rot270(sj, si, arr)
            v = [[False] * 5 for _ in range(5)]
            g = []
            sm = 0
            for i in range(5):
                for j in range(5):
                    if not v[i][j]:
                        g.append(set())
                        tmp = bfs(i, j, g, v, arr270)
                        if tmp >= 3:
                            sm += tmp
            if sm > mx:
                mx = sm
                marr = arr270
                mg = []
                for tg in g:
                    if len(tg) >= 3:
                        for ti, tj in tg:
                            mg.append((ti, tj))
    if mx > 0:
        return mx, marr, mg
    else:
        return 0, [], []

def simul(arr):

    v = [[False] * 5 for _ in range(5)]
    g = []
    mx = 0

    for i in range(5):
        for j in range(5):
            if not v[i][j]:
                g.append(set())
                tmp = bfs(i, j, g, v, arr)
                if tmp >= 3:
                    mx += tmp
    if mx > 0:
        mg = []
        for tg in g:
            if len(tg) >= 3:
                for ti, tj in tg:
                    mg.append((ti, tj))
    if mx > 0: return mx, mg
    else: return

for turn in range(1,K+1):

    a,aarr,ag = simul90(arr)
    b,barr,bg = simul180(arr)
    c,carr,cg = simul270(arr)


    if a == 0 and b == 0 and c == 0: break

    if a >= max(b,c):
        mx, marr, mg = a,aarr,ag
    elif b > a and b >= c:
        mx, marr, mg = b,barr,bg
    else:
        mx, marr, mg = c,carr,cg

    while True:
        mg.sort(key=lambda x:(x[1],-x[0]))

        for ci,cj in mg:
            marr[ci][cj] = tq.popleft()

        if not simul(marr): break

        tmp, mg = simul(marr)
        mx += tmp

    ans.append(mx)
    arr = marr

print(*ans)