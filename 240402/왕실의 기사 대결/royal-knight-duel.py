L,N,Q = map(int,input().split())
knights = {}
init_k = [0] * (N+1)
mp = [[2] * (L+2)] + [[2] + list(map(int,input().split())) + [2] for _ in range(L)] + [[2] * (L+2)]
for idx in range(1,N+1):
    r,c,h,w,k = map(int,input().split())
    knights[idx] = [r,c,h,w,k]
    init_k[idx] = k
di = [-1,0,1,0]
dj = [0,1,0,-1]
def push_knights(start,dr):

    q = []
    q.append(start)
    pset = set()
    pset.add(start)
    damage = [0] * (N+1)
    while q:
        cur = q.pop()
        ci,cj,h,w,k = knights[cur]
        # 상하좌우 중 하나로 한 칸 이동
        ni,nj = ci+di[dr], cj+dj[dr]
        # 이동해서 벽이면 모든 기사 이동 x, 함정 개수만큼 데미지
        for i in range(ni,ni+h):
            for j in range(nj,nj+w):
                if mp[i][j] == 2:
                    return
                if mp[i][j] == 1:
                    damage[cur] += 1

        # 겹치는지 확인하기
        for idx in knights:
            if idx in pset: continue # 이미 움직일 사람이면 패스
            ti,tj,th,tw,tk = knights[idx]

            if ni<=ti+th-1 and ni+h-1>=ti and nj<=tj+tw-1 and nj+w-1>=tj:
                q.append(idx)
                pset.add(idx)

    # 명령을 받은 기사는 피해를 입지 않는다.
    damage[start] = 0
    for idx in pset:
        si,sj,h,w,k = knights[idx]

        if k<=damage[idx]:
            knights.pop(idx)
        else:
            ni,nj = si + di[dr], sj + dj[dr]
            knights[idx] = ni,nj,h,w,k-damage[idx]


for _ in range(Q):
    idx, dr = map(int,input().split())
    # 왕에게 명령을 받은 기사의 움직임
    if idx in knights:
        push_knights(idx,dr)

ans = 0
for i in knights:
    ans += init_k[i] - knights[i][4]
print(ans)