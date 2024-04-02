L, N, Q = map(int,input().split())
mp = [[2] * (L+2)] + [[2] + list(map(int,input().split())) + [2] for _ in range(L)] + [[2] * (L+2)]

knights = {}
init_k = [0] * (N+1)
# 기사 정보, 초기 체력 저장 (정답 출력용)
for idx in range(1,N+1):
     r,c,h,w,k = map(int,input().split())
     knights[idx] = [r,c,h,w,k]
     init_k[idx] = k

di,dj = [-1,0,1,0], [0,1,0,-1]

def push_knights(start,dr):

    q = []
    q.append(start)
    pset = set() # visited같은 느낌
    pset.add(start)
    damage = [0] * (N+1)
    while q:
        cur = q.pop(0)
        ci,cj,h,w,k = knights[cur]

        # 상하좌우 중 한 칸 이동
        ni,nj = ci + di[dr], cj + dj[dr]

        # 기사 + h*w 방패 범위에 벽이나 함정이 있을 경우
        for i in range(ni,ni+h):
            for j in range(nj,nj+w):
                if mp[i][j] == 2: # 벽이면 return (이동 x)
                    return
                if mp[i][j] == 1:
                    damage[cur] += 1

        # 모든 전사 탐색 (겹친 경우)
        for idx in knights:
            if idx in pset: continue # 이미 밀 것이면 제외
            ti,tj,th,tw,tk = knights[idx]

            if ni <= ti+th-1 and ti <= ni+h-1 and nj <= tj+tw-1 and tj <= nj+w-1:
                q.append(idx)
                pset.add(idx)

    damage[start] = 0

    for idx in pset:
        ci,cj,h,w,k = knights[idx]

        if k <= damage[idx]:
            knights.pop(idx)

        else:
            ni,nj = ci+di[dr], cj + dj[dr]
            knights[idx] = [ni,nj,h,w,k-damage[idx]]


for _ in range(Q):
    idx, dr = map(int,input().split())
    if idx in knights:
        push_knights(idx,dr)


ans = 0
for i in range(1,N+1):
    if i in knights:
        ans += init_k[i] - knights[i][4]

print(ans)