N, M = map(int,input().split())
arr = [[1] * (N+2)] + [[1] + list(map(int,input().split())) + [1] for _ in range(N)] + [[1] * (N+2)]
# 베이스 캠프 처리
basecamp = set()
for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i][j] == 1:
            basecamp.add((i,j))
            arr[i][j] = 0
# 편의점 처리
store = {}
for m in range(1,M+1):
    i,j = map(int,input().split())
    store[m] = (i,j)

from collections import deque

def find(si,sj,dests):
    q = deque()
    v = [[False] * (N+2) for _ in range(N+2)] # 방문 경로 기록
    v[si][sj] = True
    q.append((si,sj))
    tlst = []
    while q:
        nq = deque()
        for ci,cj in q:
            if (ci,cj) in dests: # 목적지에 도착했다면
                tlst.append((ci,cj)) # 정답 처리는 for문 끝나고

            else:
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni,nj = ci + di, cj +dj
                    if not v[ni][nj] and arr[ni][nj] ==0:
                        nq.append((ni,nj))
                        v[ni][nj] = True
        q = nq

        if tlst:
            return sorted(tlst)[0]


def solve():
    time = 1
    q = deque()
    arrived = [0] * (M+1)

    while q or time ==1: # 처음엔 큐가 비어있으므로 time == 1 추가
        nq = deque()
        alst = []
        # [1] 본인이 가고 싶은 편의점 방향으로 1칸 이동 / 동일 반경으로 편의점 찾기 진행
        for ci,cj,m in q:
            if arrived[m] == 0: # 도착하지 못했다면
                ni,nj = find(store[m][0], store[m][1], set(((ci-1,cj),(ci+1,cj),(ci,cj-1),(ci,cj+1))))
                if (ni,nj) == store[m]: # 편의점에 도착
                    arrived[m] = time # 도착한 시간 기록
                    alst.append((ni,nj))
                else:
                    nq.append((ni,nj,m)) # 이동 진행
        q = nq


        # [2] 만약 편의점에 도착한다면 해당 편의점에서 멈추고, 지나갈 수 없게 만들기
        if alst:
            for ai, aj in alst:
                arr[ai][aj] = 1

        # [3] time<=m 일 때, 자신이 가고싶어 하는 베이스 캠프로 이동
        if time <=M:
            si,sj = store[time] # m번 사람이 가고싶어 하는 위치
            ei,ej = find(si,sj,basecamp) # 베이스 캠프의 위치
            basecamp.remove((ei,ej))
            arr[ei][ej] = 1 # 베이스 캠프도 이동처리
            q.append((ei,ej,time))

        time += 1

    return max(arrived)

ans = solve()
print(ans)