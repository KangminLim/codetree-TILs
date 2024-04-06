L,N,Q = map(int,input().split())
knight = {}
arr = [[2]*(L+2)] + [[2] + list(map(int,input().split())) + [2] for _ in range(L)] + [[2]*(L+2)]
init_k = [0] * (N+1)

for idx in range(1,N+1):
    r,c,h,w,k = map(int,input().split())
    knight[idx] = [r,c,h,w,k]
    init_k[idx] = k

di,dj = [-1,0,1,0], [0,1,0,-1]

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

        # 상하좌우 한 칸 이동
        ni, nj = ci+di[dr],cj+dj[dr]

        # 벽 or 함정을 만났을 때
        for i in range(ni,ni+h):
            for j in range(nj,nj+w):
                if arr[i][j] == 2: # 벽 만나면 끝
                    return
                elif arr[i][j] == 1: # 함정이면 데미지
                    damage[cur] += 1

        # 전체 기사 탐색해서 연쇄 작용
        for idx in knight:
            if idx in kset: continue # 이미 밀 예정인 기사는 제외
            ti, tj, th, tw, k = knight[idx]

            # 겹치면 q에 추가
            if ni<=ti+th-1 and ti <= ni+h-1 and nj <= tj+tw-1 and tj <=nj+w-1:
                q.append(idx)
                kset.add(idx)

    # 명령을 받은 기사는 데미지 제외
    damage[start] = 0

    for idx in kset:
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