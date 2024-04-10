L, N, Q = map(int,input().split())
arr = [[2] * (L+2)]+[[2] + list(map(int,input().split())) + [2] for _ in range(L)] + [[2] * (L+2)]
knight = {}
init_k = [0] * (N+1)
for idx in range(1,N+1):
    i,j,h,w,k = map(int,input().split())
    knight[idx] = [i,j,h,w,k]
    init_k[idx] = k
di,dj = [-1,0,1,0], [0,1,0,-1]

from collections import deque
def push_knight(start,dr):
    q = deque()
    q.append(start)
    pset = set()
    pset.add(start)
    damage = [0] * (N + 1)

    while q:
        cur = q.popleft()
        ci, cj, ch, cw, ck = knight[cur]
        ni, nj = ci + di[dr], cj + dj[dr]

        for i in range(ni, ni + ch):
            for j in range(nj, nj + cw):
                if arr[i][j] == 2:
                    return
                elif arr[i][j] == 1:
                    damage[cur] += 1

        for idx in knight:
            if idx not in pset:
                ti,tj,th,tw,tk = knight[idx]

                if ni <= ti+th-1 and ti <= ni+ch-1 and nj <= tj+tw-1 and tj <= nj+cw-1:
                    q.append(idx)
                    pset.add(idx)

    damage[start] = 0

    for idx in pset:
        ci,cj,h,w,k = knight[idx]

        if k <= damage[idx]:
            knight.pop(idx)

        else:
            ni,nj = ci+di[dr], cj+dj[dr]
            knight[idx] = [ni,nj,h,w,k-damage[idx]]


for _ in range(Q):
    idx, dr = map(int,input().split())
    if idx in knight:
        push_knight(idx,dr)

ans = 0
for idx in knight:
    ans += init_k[idx] - knight[idx][4]

print(ans)