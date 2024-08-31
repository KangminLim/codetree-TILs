L, N, Q = map(int,input().split())
arr = [[2] * (L+2)] + [[2] + list(map(int,input().split())) + [2] for _ in range(L)] + [[2] * (L+2)]
knights = {}
init_k = [0] * (N+1)
for idx in range(1,N+1):
    r,c,h,w,k = map(int,input().split())
    knights[idx] = [r,c,h,w,k]
    init_k[idx] = k
di,dj = [-1,0,1,0], [0,1,0,-1]
from collections import deque
def bfs(start, cd):
    q = deque()
    q.append(start)
    damage = [0] * (N+1)
    # 연쇄 처리를 위한 fset 추가
    fset = set()
    fset.add(start)
    while q:
        cur = q.popleft()
        ci,cj,ch,cw,ck = knights[cur]
        ni,nj = ci+di[cd], cj+dj[cd]
        # 1. 2중 for문(데미지 및 벽 처리)
        for i in range(ni,ni+ch):
            for j in range(nj,nj+cw):
                if arr[i][j] == 2:
                    return
                elif arr[i][j] == 1:
                    damage[cur] += 1
        # 2. 이동 후 모든 knight 순회
        for idx in knights:
            if idx not in fset:
                ti,tj,th,tw,tk = knights[idx]
                # if ni <= ti + th - 1 and nj <= tj + tw - 1 and ti <= ni + ch - 1 and tj <= nj + cw - 1:
                #     q.append(idx)
                #     fset.add(idx)
                # if ni <= ti+th-1 and nj <= tj+tw-1 and ti <= ni+ch-1 and tj <= nj+cw-1:
                #     q.append(idx)
                #     fset.add(idx)
                if (ni <= ti <= ni + ch - 1 or ti <= ni <= ti + th - 1) and (tj <= nj <= tj + tw - 1 or nj <= tj <= nj + cw - 1 ):
                    q.append(idx)
                    fset.add(idx)
    damage[start] = 0
    for idx in fset:
        ci,cj,ch,cw,ck = knights[idx]
        if ck - damage[idx] <= 0:
            knights.pop(idx)
        else:
            knights[idx] = [ci+di[cd],cj+dj[cd],ch,cw,ck-damage[idx]]

for turn in range(Q):
    idx, dr = map(int,input().split())
    if idx in knights:
        bfs(idx,dr)

ans = 0
for idx in knights:
    ans += init_k[idx] - knights[idx][4]

print(ans)