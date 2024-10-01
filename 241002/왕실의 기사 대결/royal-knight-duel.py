L, N, Q = map(int,input().split())
arr = [[2] * (L+2)] + [[2] + list(map(int,input().split())) + [2] for _ in range(L)] + [[2] * (L+2)]
knights = {}
init_k = [0] * (N+1)
for idx in range(1,N+1):
    r,c,h,w,k = map(int,input().split())
    knights[idx] = [r,c,h,w,k]
    init_k[idx] = k

di,dj = [-1,0,1,0],[0,1,0,-1]

from collections import deque
def push_knight(start,dr):
    q = deque()
    q.append(start)
    fset = set()
    fset.add(start)
    damage = [0] * (N+1)

    while q:
        cur = q.popleft()
        ci,cj,ch,cw,ck = knights[cur]
        ni,nj = ci+di[dr],cj+dj[dr]
        for i in range(ni,ni+ch):
            for j in range(nj,nj+cw):
                if arr[i][j] == 2:
                    return
                elif arr[i][j] == 1:
                    damage[cur] += 1

        for idx in knights:
            if idx not in fset:
                ti,tj,th,tw,tk = knights[idx]
                if (ti<=ni<ti+th or ni <= ti < ni+ch) and (tj<=nj<tj+tw or nj<=tj<nj+cw):
                    q.append(idx)
                    fset.add(idx)
    damage[start] = 0

    for idx in fset:
        ci,cj,ch,cw,ck = knights[idx]
        if ck - damage[idx] <= 0:
            knights.pop(idx)
        else:
            knights[idx] = [ci+di[dr],cj+dj[dr],ch,cw,ck-damage[idx]]


for _ in range(Q):
    idx, dr = map(int,input().split())
    if idx in knights:
        push_knight(idx,dr)

ans = 0

for idx in knights:
    ans += init_k[idx] - knights[idx][4]

print(ans)