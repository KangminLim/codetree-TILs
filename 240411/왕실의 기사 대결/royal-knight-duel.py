L, N, Q = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(L)]

knight = {}
init_k = [0] * (N+1)

for idx in range(1, N+1):
    i,j,h,w,k = map(int,input().split())
    knight[idx] = [i-1,j-1,h,w,k]
    init_k[idx] = k
di,dj = [-1,0,1,0], [0,1,0,-1]

from collections import deque
def push_knights(start,dr):
    q = deque()
    q.append(start)
    damage = [0] * (N+1)
    pset = set()
    pset.add(start)
    while q:
        # 기사의 이동
        cur = q.popleft()
        ci,cj,h,w,k = knight[cur]
        ni,nj = ci+di[dr], cj+dj[dr]
        
        if 0<=ni<N and 0<=nj<N: # 범위 내
            # 이동한 위치에서 함정 피해 or 벽
            for i in range(ni,ni+h):
                for j in range(nj,nj+w):
                    # 벽을 만나면 모든 기사 이동 불가
                    if arr[i][j] == 2:
                        return
                    # w x h 함정의 수만큼 피해 입음
                    elif arr[i][j] == 1:
                        damage[cur] += 1

        # 이동한 위치와 겹치는 기사가 있는지 확인
        for idx in knight:
            # 이미 밀 예정인 기사는 pass
            if idx in pset: continue

            ti, tj, th, tw, k = knight[idx]

            if ni <= ti+th-1 and ti <= ni+h-1 and nj <= tj+tw-1 and tj <= nj+w-1:
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
    idx,dr = map(int,input().split())
    if idx in knight:
        push_knights(idx,dr)

ans = 0
for m in range(1,N+1):
    if m in knight:
        ans += init_k[m] - knight[m][4]

print(ans)