N, M = map(int,input().split())
arr = [[1] * (N+2)] + [[1] + list(map(int,input().split())) + [1] for _ in range(N)] + [[1] * (N+2)]

basecamp = set()

# 베이스 캠프 처리
for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i][j] == 1:
            basecamp.add((i,j))
            arr[i][j] = 0 # 맵에서 지움 [3] 이후 부터 맵에 새김

store = {}
for m in range(1,M+1):
    i,j = map(int,input().split())
    store[m] = (i,j)

from collections import deque

def find(si,sj,dests):
    q = deque()
    q.append((si,sj))
    v = [[False] * (N+2) for _ in range(N+2)]
    v[si][sj] = 1
    tlst = []
    while q:
        nq = deque()
        for ci,cj in q:
            if (ci,cj) in dests: # 큐가 목적지에 도착했으면
                tlst.append((ci,cj))
            else:
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni, nj = ci+di, cj+dj
                    if not v[ni][nj] and arr[ni][nj] == 0:
                        nq.append((ni,nj))
                        v[ni][nj] = True
        q = nq

        # 목적지에 도착했으면 정렬해서 return -> 행이 작고 열이 작은 순으로 찾아줌
        if tlst:
            return sorted(tlst)[0]

# 가장 가까운 베이스 캠프를 찾고, 편의점을 찾아야 하므로 2중 deque 구조로 동일 반경 탐색 진행
def solve():
    q = deque()
    time = 1
    arrived = [0] * (M+1)

    while q or time == 1: # time == 1일 때와 q 진행
        nq = deque()
        alst = []
        # [1] 격자 모든 사람 편의점 방향으로 이동
        for ci,cj,m in q:
            if arrived[m] == 0: # 편의점 도착하지 못했다면
                # 본인이 가고싶은 편의점 방향을 향해 1칸 움직임
                ni,nj = find(store[m][0], store[m][1], set(((ci-1,cj),(ci+1,cj),(ci,cj-1),(ci,cj+1))))
                if (ni,nj) == store[m]: # 편의점에 도착했다면
                    alst.append((ni,nj)) # 도착 처리는 뒤에서 진행
                    arrived[m] = time # 도착 시간
                else:
                    nq.append((ni,nj,m)) # 게속 이동

        q = nq

        # [2] 편의점에 도착했으면 해당 편의점에서 멈추고, 움직일 수 없는 처리 진행
        if alst:
            for ai, aj in alst:
                arr[ai][aj] = 1

        # [3] t<=M 을 만족하면 t번 사람은 t번이 가고 싶어하는 편의점과 가장 가까운 베이스 캠프로 들어감
        # 동일반경 탐색에서는 내가 가고싶은 곳에서 좌표를 찾는게 낫다
        if time <= M:
            si,sj = store[time] # 편의점 좌표
            ei,ej = find(si,sj,basecamp) # 베이스 캠프 좌표
            basecamp.remove((ei,ej))
            q.append((ei,ej,time))
            arr[ei][ej] = 1

        time += 1

    return max(arrived)

ans = solve()
print(ans)