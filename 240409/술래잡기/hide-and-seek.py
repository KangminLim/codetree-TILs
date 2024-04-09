N,M,H,K = map(int,input().split())

people = {}
for m in range(1,M+1):
    i,j,dr = map(int,input().split())
    people[m] = [i,j,dr]
is_live = [True] * (M+1)
is_live[0] = False

di,dj = [0,0,1,-1], [-1,1,0,0]
opp = {0:1, 1:0, 2:3, 3:2}
tree = set()
tm = (N+1)//2

ti,tj,td = tm,tm,0
tdi,tdj = [-1,0,1,0], [0,1,0,-1]

mx_cnt, cnt, flag, val = 1,0,0,1
for _ in range(H):
    i,j = map(int,input().split())
    tree.add((i,j))
narr = [[0] * (N+2) for _ in range(N+2)]

ans = 0

for k in range(1,K+1):
    # [1] 도망자의 이동
    for i in people:
        if not is_live[i]: continue
        ci,cj,cd = people[i]
        if abs(ci-ti) + abs(cj-tj) <= 3:
            ni,nj = ci+di[cd], cj+dj[cd]
            if 1<=ni<=N and 1<=nj<=N:
                if (ni,nj) != (ti,tj):
                    people[i] = [ni,nj,cd]
            else:
                nd = opp[cd]
                ni,nj = ci+di[nd], cj+dj[nd]
                if (ni,nj) != (ti,tj):
                    people[i] = [ni,nj,nd]
    # [2] 술래의 이동
    cnt += 1
    narr[ti][tj] = k

    ti,tj = ti+tdi[td], tj+tdj[td]

    if (ti,tj) == (1,1):
        mx_cnt, cnt, flag, val = N, 1, 1, -1
        td = 2
    elif (ti,tj) == (tm,tm):
        mx_cnt, cnt, flag, val = 1, 0, 0, 1
        td = 0

    else:
        if mx_cnt == cnt:
            cnt = 0
            td = (td+val)%4

            if flag ==0:
                flag = 1
            else:
                flag = 0
                mx_cnt += val

    # [3] 술래 잡기
    tset = set(((ti,tj),(ti+tdi[td],tj+tdj[td]),(ti+tdi[td]*2, tj+tdj[td]*2)))
    for idx in people:
        if not is_live[idx] : continue
        ci,cj,cd = people[idx]
        if (ci,cj) in tset and (ci,cj) not in tree:
            ans += k
            is_live[idx] = False


print(ans)