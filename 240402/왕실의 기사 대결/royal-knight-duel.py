L, N, Q = map(int,input().split())
mp = [[2] * (L+2)] + [[2] + list(map(int,input().split())) + [2] for _ in range(L)] + [[2] * (L+2)]

knights = {}
init_k = [0] * (N+1)
for idx in range(1,N+1):
    r,c,h,w,k = map(int,input().split())
    knights[idx] = [r,c,h,w,k]
    init_k[idx] = k

di,dj = [-1,0,1,0],[0,1,0,-1]

def push_knight(start,dr):
    q = []
    pset = set()
    q.append(start)
    pset.add(start)
    damage = [0] * (N+1)
    while q:
        cur = q.pop()
        ci,cj,h,w,k = knights[cur]
        ni,nj = ci+di[dr], cj+dj[dr]
        for i in range(ni,ni+h):
            for j in range(nj,nj+w):
                if mp[i][j] == 2: # 벽이면 이동 x
                    return
                if mp[i][j] == 1: # 함정이면 개수만큼 데미지 쌓이기
                    damage[cur] += 1
        # 모든 기사와 겹치는 것 확인
        for idx in knights:
            if idx in pset: continue # 움직일 사람이면 pass
            ti,tj,th,tw,k = knights[idx]

            if ni<=ti+th-1 and ni+h-1<=ti and nj+w-1<=tj and nj <= tj+tw-1:
                q.append(idx)
                pset.add(idx)
    # 데미지 계산

    for idx in pset:
        ci,cj,h,w,k = knights[idx]

        if k < damage[idx]:
            knights.pop(idx)

        else:
            ni,nj = ci+di[dr],cj+dj[dr]
            knights[idx] = [ni,nj,h,w,k-damage[idx]]


for _ in range(Q):
    idx, dr = map(int,input().split())
    if idx in knights: # 죽으면 knight에서 빼므로
        push_knight(idx,dr)

ans = 0
for idx in knights:
    ans += init_k[idx] - knights[idx][4]
print(ans)