N,M,P,C,D = map(int,input().split())
ri,rj = map(lambda x:int(x)-1,input().split())
santa = {}
arr = [[0] * N for _ in range(N)]
arr[ri][rj] = -1
stun = [0] * (P+1)
scores = [0] * (P+1)
live = [True] * (P+1)
live[0] = False

for _ in range(P):
    sn,si,sj = map(int,input().split())
    santa[sn] = [si-1,sj-1]
    arr[si-1][sj-1] = sn

from collections import deque

def santa_move(cur,ci,cj,cdi,cdj,mul):
    q = deque()
    q.append((cur,ci,cj,mul))

    while q:
        cur,ci,cj,mul = q.popleft()
        ni,nj = ci+cdi*mul,cj+cdj*mul

        if 0<=ni<N and 0<=nj<N: # 범위 내
            if arr[ni][nj] == 0:
                santa[cur] = [ni, nj]
                arr[ni][nj] = cur
            else:
                q.append((arr[ni][nj], ni, nj, 1))
                santa[cur] = [ni, nj]
                arr[ni][nj] = cur
        else:  # 범위 밖
            live[cur] = False


for turn in range(1,M+1):
    # 모두 탈락하면 게임 끝
    if live.count(True) == 0: break
    # 1. 루돌프 이동
    # 1.1 돌진할 산타 정하기
    mdist = 2 * N * N
    for i in range(1, P + 1):
        if not live[i]: continue  # 탈락한 산타는 제외
        # 산타 좌표
        ci, cj = santa[i]
        dist = (ri - ci) ** 2 + (rj - cj) ** 2
        if mdist > dist:
            mdist = dist
            tlst = [(ci, cj, i)]
        elif mdist == dist:
            tlst.append((ci, cj, i))

    tlst.sort(key=lambda x: (-x[0], -x[1]))
    # 돌진할 산타 선정
    si, sj, sn = tlst[0]

    # 1.2 루돌프 이동 진행을 위한 rdi, rdj 설정
    rdi, rdj = 0, 0
    if ri > si:
        rdi = -1
    elif ri < si:
        rdi = 1

    if rj > sj:
        rdj = -1
    elif rj < sj:
        rdj = 1

    arr[ri][rj] = 0  # 루돌프 이동 처리
    ri, rj = ri + rdi, rj + rdj
    arr[ri][rj] = -1  # 루돌프 이동 처리

    if (ri, rj) == (si, sj):
        stun[sn] = turn + 2
        scores[sn] += C
        santa_move(sn, si, sj, rdi, rdj, C)


    # 2. 산타 이동
    for i in range(1, P + 1):
        if not live[i]: continue  # 탈락한 산타는 제외
        if stun[i] > turn: continue  # 기절의 경우 이동 불가
        ci, cj = santa[i]
        min_dist = (ri - ci) ** 2 + (rj - cj) ** 2
        mlst = []
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] <= 0:  # 범위 내, 산타가 없는
                dist = (ri - ni) ** 2 + (rj - nj) ** 2
                if min_dist > dist:
                    min_dist = dist
                    mlst.append((ni, nj, di, dj))
        if not mlst:
            continue
        ni,nj,cdi,cdj = mlst[-1] # 가장 마지막 리스트 요소가 최단거리
        if (ni,nj) == (ri,rj):
            stun[i] = turn+2
            scores[i] += D
            arr[ci][cj] = 0
            santa_move(i,ni,nj,-cdi,-cdj,D)
        else:
            santa[i] = [ni,nj]
            arr[ci][cj] = 0 # 이동 처리
            arr[ni][nj] = i



    for i in range(1,P+1):
        if live[i]:
            scores[i] += 1

for i in range(1,P+1):
    print(scores[i],end=' ')