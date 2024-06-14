L, N, Q = map(int,input().split())
arr = [[2] * (L+2)] + [[2] + list(map(int,input().split())) + [2] for _ in range(L)] + [[2] * (L+2)]
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
    damage = [0] * (N+1)
    fset = set()
    fset.add(start)
    while q:
        cur = q.popleft()
        ci,cj,ch,cw,ck = knight[cur]
        ni,nj = ci+di[dr],cj+dj[dr]

        for i in range(ni,ni+ch):
            for j in range(nj,nj+cw):
                if arr[i][j] == 1: # 함정 개수만큼 +1
                    damage[cur] += 1
                elif arr[i][j] == 2: # 벽을 만나면 이동 취소
                    return

        # 기사가 이동하려는 위치에 다른 기사가 있다면 그 기사도 이동시킴
        for i in knight:
            if i not in fset:
                ti,tj,th,tw,tk = knight[i]

                if ni<=ti+th-1 and nj<=tj+tw-1 and ti <= ni+ch-1 and tj <= nj+cw-1:
                    q.append(i)
                    fset.add(i)

    damage[start] = 0
    for idx in range(1,N+1):
        if idx in fset:
            ci,cj,ch,cw,ck = knight[idx]
            if ck - damage[idx] >0:
                knight[idx] = [ci+di[dr],cj+dj[dr],ch,cw,ck-damage[idx]]
            else:
                knight.pop(idx)


for _ in range(Q):
    idx, dr = map(int,input().split())
    push_knight(idx,dr)

ans = 0
for i in range(1,N+1):
    if i in knight:
        ans += init_k[i] - knight[i][4]

print(ans)