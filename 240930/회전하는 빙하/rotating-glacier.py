N, Q = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(2**N)]
rlst = list(map(int,input().split()))
for i in range(Q):
    l = rlst[i]
    L = 2**l
    narr = [x[:] for x in arr]
    HL = 2**(l-1)
    if l != 0:
        for si in range(0,2**N,L):
            for sj in range(0,2**N,L):
                for dr in range(4):
                    if dr == 0:
                        for i in range(HL):
                            for j in range(HL):
                                narr[si+i][sj+HL+j] = arr[si+i][sj+j]
                    elif dr == 1:
                        for i in range(HL):
                            for j in range(HL):
                                narr[si+HL+i][sj+HL+j] = arr[si+i][sj+HL+j]
                    elif dr == 2:
                        for i in range(HL):
                            for j in range(HL):
                                narr[si+HL+i][sj+j] = arr[si+HL+i][sj+HL+j]
                    else:
                        for i in range(HL):
                            for j in range(HL):
                                narr[si+i][sj+j] = arr[si+HL+i][sj+j]
    arr = narr

    narr = [x[:] for x in arr]

    for i in range(2**N):
        for j in range(2**N):
            if arr[i][j] > 0:
                cnt = 0
                for ni,nj in ((i-1,j),(i,j+1),(i+1,j),(i,j-1)):
                    if 0<=ni<2**N and 0<=nj<2**N and arr[ni][nj] > 0:
                        cnt += 1
                if cnt < 3:
                    narr[i][j] -= 1
    arr = narr

ans1 = 0
for lst in arr:
    ans1 += sum(lst)

from collections import deque
def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v[si][sj] = True
    cnt = 1
    while q:
        ci,cj = q.popleft()
        for ni, nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if 0<=ni<2**N and 0<=nj<2**N and not v[ni][nj] and arr[ni][nj]>0:
                v[ni][nj] = True
                q.append((ni,nj))
                cnt += 1
    return cnt

ans2 = 0
v = [[False] * 2**N for _ in range(2**N)]
for i in range(2**N):
    for j in range(2**N):
        if not v[i][j] and arr[i][j] >0:
            tmp = bfs(i,j)
            if tmp > ans2:
                ans2 = tmp
print(ans1)
print(ans2)