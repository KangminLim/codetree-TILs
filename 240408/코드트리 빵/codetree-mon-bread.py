N, M = map(int,input().split())
basecamp = set()

arr = [[1] * (N+2)] + [[N] + list(map(int,input().split())) + [N] for _ in range(N)] + [[1] *(N+2)]
for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i][j] == 1:
            basecamp.add((i,j))
            arr[i][j] = 0

store = {}
for m in range(1,M+1):
    i,j = map(int,input().split())
    store[m] = [i,j]


from collections import deque
def find(si,sj,dests):
    q = deque()
    q.append((si,sj))
    v = [[False] * (N+2) for _ in range(N+2)]
    v[si][sj] = True
    tlst = []
    while q:
        nq = deque()
        for ci,cj in q:
            if (ci,cj) in dests:
                tlst.append((ci,cj))

            else:
                for ni,nj in ((ci-1,cj),(ci,cj-1),(ci,cj+1),(ci+1,cj)):
                    if arr[ni][nj] ==0 and not v[ni][nj]:
                        nq.append((ni,nj))
                        v[ni][nj] = True
        q = nq

        if tlst:
            tlst.sort()
            return tlst[0]


def solve():
    time = 1
    q = deque()
    arrived = [0] * (M+1)
    while q or time==1:
        nq = deque()
        alst = []
    # [1] 본인이 가고 싶어하는 편의점 방향을 향해 1칸 움직이기
        for ci, cj, m in q:
            if arrived[m] == 0:
                ni,nj = find(store[m][0],store[m][1],set(((ci-1,cj),(ci,cj-1),(ci,cj+1),(ci+1,cj))))
                if [ni,nj] == store[m]:
                    arrived[m] = time
                    alst.append((ni,nj))
                else:
                    nq.append((ni,nj,m))
        q = nq

    # [2] 도착한 편의점은 이동 불가 처리
        if alst:
            for ai,aj in alst:
                arr[ai][aj] = 1

    # [3] 현재 시간이 t분이고 t<=m
    # 자신이 가고 싶어하는 편의점과 가장 가까이 있는 베이스 캠프에 들어가기
        if time <=M:
            si,sj = store[time]
            ei,ej = find(si,sj,basecamp)
            basecamp.remove((ei,ej))
            arr[ei][ej] = 1
            q.append((ei,ej,time))
        time += 1

    return max(arrived)

ans = solve()

print(ans)