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
def move_knight(start,dr):
    q = deque()
    q.append(start)
    damage = [0] * (N+1)
    kset = set()
    kset.add(start)

    while q:
        cur = q.popleft()
        ci,cj,ch,cw,ck = knights[cur]
        ni,nj = ci+di[dr], cj+dj[dr]

        # 2중 for문
        for i in range(ni,ni+ch):
            for j in range(nj,nj+cw):
                if arr[i][j] == 2: return
                elif arr[i][j] == 1:
                    damage[cur] += 1

        # 기사 겹치는 것 확인
        for idx in knights:
            if idx not in kset:
                ti,tj,th,tw,tk = knights[idx]
                if ni <= ti < ni+ch or nj <= tj < nj+cw or ti <= ni < ti+th or tj <= nj < tj+tw:
                    q.append(idx)
                    kset.add(idx)
    damage[start] = 0

    for idx in range(1,N+1):
        if idx in knights:
            ci,cj,ch,cw,ck = knights[idx]
            if ck - damage[idx] > 0:
                knights[idx] = [ci+di[dr],cj+dj[dr],ch,cw,ck-damage[idx]]
            else:
                knights.pop(idx)

for turn in range(1,Q+1):
    idx,dr = map(int,input().split())
    move_knight(idx,dr)

ans = 0
for idx in knights:
    ans += init_k[idx] - knights[idx][4]
print(ans)