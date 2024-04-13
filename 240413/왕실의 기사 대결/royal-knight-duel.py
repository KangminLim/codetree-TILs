L, N, Q = map(int,input().split())
arr = [[2] * (L+2)] + [[2] + list(map(int,input().split())) + [2] for _ in range(L)] + [[2] * (L+2)]
init_k = [0] * (N+1)
knight = {}
for idx in range(1,N+1):
    i,j,h,w,k = map(int,input().split())
    knight[idx] = [i,j,h,w,k]
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
        ci,cj,h,w,k = knight[cur]
        ni,nj = ci+di[dr],cj+dj[dr]

        for i in range(ni,ni+h):
            for j in range(nj,nj+w):
                # if not (1<=i<=N and 1<=j<=N): return # 범위 벗어나면 종료
                if arr[i][j] == 1:
                    damage[cur] += 1
                elif arr[i][j] == 2:
                    return

        for idx in knight:
            if idx in fset: continue
            ti,tj,th,tw,_ = knight[idx]

            if ni <= ti+th-1 and nj <=tj+tw-1 and ti <= ni+h-1 and tj <= nj+w-1:
                q.append(idx)
                fset.add(idx)

    damage[start] = 0

    for idx in fset:
        ci,cj,h,w,k = knight[idx]

        if k <= damage[idx]:
            knight.pop(idx)
        else:
            ni,nj = ci+di[dr], cj+dj[dr]
            knight[idx] = [ni,nj,h,w,k-damage[idx]]


for _ in range(Q):
    idx,dr = map(int,input().split())
    if idx in knight:
        push_knight(idx,dr)

ans = 0
for idx in knight:
    ans += init_k[idx] - knight[idx][4]
print(ans)