N, M, C = map(int,input().split())
arr = [[-1] * (N+2)] + [[-1] + list(map(int,input().split())) + [-1] for _ in range(N)] + [[-1] * (N+2)]
for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i][j] == 1:
            arr[i][j] = -1
ti,tj = map(int,input().split())
# arr[ti][tj] = -2
s_set = set()
e_dict = {}
for i in range(1,M+1):
    si,sj,ei,ej = map(int,input().split())
    arr[si][sj] = i
    s_set.add((si,sj))
    e_dict[i] = (ei,ej)

from collections import deque

def find(si,sj,dest):
    q = deque()
    q.append((si,sj,0))
    v = [[False] * (N+2) for _ in range(N+2)]
    v[si][sj] = True
    cnt = 0
    while q:
        tlst = []
        nq = deque()
        cnt += 1
        for ci, cj, m in q:
            if (ci,cj) in dest:
                tlst.append((ci,cj,m))
            else:
                for ni, nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
                    if arr[ni][nj] >= 0 and not v[ni][nj]:
                        nq.append((ni,nj,cnt))
                        v[ni][nj] = True
        q = nq
        if tlst:
            return sorted(tlst,key=lambda x:(x[2],x[0],x[1]))[0]
    return False

flag = True
# while e_dict:
for _ in range(1,M+1):

    if not find(ti, tj, s_set):
        flag = False
        break
    else:
        si, sj, cnt = find(ti, tj, s_set)

    if C - cnt < 0:
        flag = False
        break
    C -= cnt

    s_set.remove((si,sj))
    num = arr[si][sj]
    tdi,tdj = e_dict[num]
    e_dict.pop(num)

    if not find(si,sj,set(((tdi,tdj),(0,0)))):
        flag = False
        break
    else:
        ei, ej, cnt = find(si, sj, set(((tdi, tdj), (0, 0))))

    if C - cnt < 0:
        flag = False
        break

    C += cnt

    ti,tj = ei,ej

if not flag:
    print(-1)
else:
    print(C)