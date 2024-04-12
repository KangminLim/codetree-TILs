L, N, Q = map(int,input().split())
arr = [[1]*(L+2)] + [[1] + list(map(int,input().split())) + [1] for _ in range(L)] + [[1] * (L+2)]
knight = {}
init_k = [0] * (N+1)
for idx in range(1,N+1):
    i,j,h,w,k = map(int,input().split())
    knight[idx] = [i,j,h,w,k]
    init_k[idx] = k
di,dj = [-1,0,1,0], [0,1,0,-1]
ans = 0
from collections import deque
def push_knight(start,dr):
    q = deque()
    q.append(start)
    kset = set()
    kset.add(start)
    damage = [0] * (N+1)
    while q:
        cur = q.popleft()
        ci,cj,h,w,k = knight[cur]
        ni,nj = ci+di[dr], cj+dj[dr]
        if 1<=ni<=N and 1<=nj<=N:
            # 기사의 함정과 벽 탐색
            for i in range(ni,ni+h):
                for j in range(nj,nj+w):
                    if arr[i][j] == 1: # 함정을 만나면
                        damage[cur] += 1
                    elif arr[i][j] == 2: # 벽을 만나면, 모든 명령 취소
                        return

            for idx in knight:
                if idx in kset: continue

                ti,tj,th,tw,_ = knight[idx]

                if ni <= ti+th-1 and nj <= tj+tw-1 and ti <= ni+h-1 and tj <= nj+w-1:
                    q.append(idx)
                    kset.add(idx)

    damage[start] = 0

    for idx in kset:
        ci,cj,h,w,k = knight[idx]

        if k <= damage[idx]:
            knight.pop(idx)

        else:
            ni,nj = ci+di[dr], cj+dj[dr]
            knight[idx] = [ni,nj,h,w,k-damage[idx]]


for _ in range(1,Q+1):
    idx,dr = map(int,input().split())
    if idx in knight:
        push_knight(idx,dr)

for idx in knight:
    ans += init_k[idx]-knight[idx][4]

print(f'{ans}')