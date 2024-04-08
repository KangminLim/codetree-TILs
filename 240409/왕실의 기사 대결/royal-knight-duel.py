L, N, Q = map(int,input().split())

arr = [[2] * (L+2)] + [[2]+list(map(int,input().split()))+[2] for _ in range(L)] + [[2] * (L+2)]

knights = {}
init_k = [0] * (N+1)


for idx in range(1,N+1):
    i,j,h,w,k = map(int,input().split())
    knights[idx] = [i,j,h,w,k]
    init_k[idx] = k

di, dj = [-1,0,1,0], [0,1,0,-1]

from collections import deque

def push_knight(start,dr):
    q = deque()
    q.append(start)
    damage = [0] * (N+1)
    pset = set()
    pset.add(start)
    while q:
        cur = q.popleft()
        # [1] 기사 이동 : 왕에게 명령을 받은 기사는 상하좌우 중 한 칸 이동
        ci,cj,h,w,k = knights[cur]

        ni,nj = ci+di[dr], cj+dj[dr]


        # 이동한 위치 벽이 있다면 모든 기사 이동 x / 함정 개수 만큼 데미지
        for i in range(ni,ni+h):
            for j in range(nj,nj+w):
                if arr[i][j] == 2:
                    return
                elif arr[i][j] ==1:
                    damage[cur] += 1

        # 이동 후 거기에 있는 기사와 겹치는지 확인
        for idx in knights:
            if idx not in pset:
                ti,tj,th,tw,tk = knights[idx]

                if ni <= ti+th-1 and ti<=ni+h-1 and nj <= tj+tw-1 and tj<=nj+w-1:
                    q.append(idx)
                    pset.add(idx)


    damage[start] = 0
    for idx in pset:
        ci,cj,h,w,k = knights[idx]

        if k <= damage[idx]:
            knights.pop(idx)

        else:
            ni,nj = ci+di[dr], cj+dj[dr]
            knights[idx] = [ni,nj,h,w,k-damage[idx]]


for _ in range(1, Q+1):
    idx, dr = map(int,input().split())
    if idx in knights:
        push_knight(idx,dr)

ans = 0
for idx in knights:
    ans += init_k[idx] - knights[idx][4]
print(ans)