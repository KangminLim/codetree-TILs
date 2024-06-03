L, N, Q = map(int,input().split())
arr = [[2] * (L+2) ] + [[2]+ list(map(int,input().split())) + [2] for _ in range(L)] + [[2] * (L+2)]
knight = {}
init_k = [0] * (N+1)

for i in range(1,N+1):
    r,c,h,w,k = map(int,input().split())
    knight[i] = [r,c,h,w,k]
    init_k[i] = k
di,dj = [-1,0,1,0], [0,1,0,-1]

from collections import deque

def knight_duel(idx,dr):
    q = deque()
    q.append(idx)
    dset = set()
    dset.add(idx)
    damage = [0] * (N + 1)
    while q:
        cur_num = q.popleft()
        ci,cj,ch,cw,ck = knight[cur_num]
        # 2.1 기사 이동
        ni,nj = ci+di[dr], cj+dj[dr]
        # if not (0<=ni<N and 0<=nj<N): return
        # 2.3 이동한 위치에서 함정 혹은 벽 유무 확인
        for i in range(ni,ni+ch):
            for j in range(nj,nj+cw):
                if arr[i][j] == 1:
                    damage[cur_num] += 1
                elif arr[i][j] == 2:
                    return # 벽이면 모든 기사 취소

        # 2.2 연쇄 이동
        for num in knight:
            if num not in dset:
                ti,tj,th,tw,tk = knight[num]
                if ti<=ni+ch-1 and tj<=nj+cw-1 and ni<=ti+th-1 and nj<=tj+tw-1:
                    q.append(num)
                    dset.add(num)

    # 2.3 데미지 처리
    damage[idx] = 0

    for num in dset:
        ci,cj,ch,cw,ck = knight[num]
        ck -= damage[num]
        if ck <= 0:
            knight.pop(num)
        else:
            knight[num] = [ci+di[dr],cj+dj[dr],ch,cw,ck]



for turn in range(Q):
    idx, dr = map(int,input().split())
    if idx in knight:
        knight_duel(idx,dr)

ans = 0
for i in knight:
    ans += init_k[i] - knight[i][4]
print(ans)