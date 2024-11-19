N, M, K = map(int,input().split())
lst = []
for _ in range(M):
    si,sj,sm,ss,sd = map(int,input().split())
    lst.append((si,sj,sm,ss,sd))


di, dj = [-1,-1,0,1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1]

for turn in range(1,K+1):

    # 1. 모든 원자 이동(for문)
    # 자신의 방향, 속력
    for i in range(len(lst)):
        ci,cj,cm,cs,cd = lst[i]
        ni,nj = (ci + di[cd] * cs) % N, (cj + dj[cd] * cs) % N
        lst[i] = (ni,nj,cm,cs,cd)

    # 2. 원자 합성
    lst.sort()
    lst.append((100,100,1001,1001,9)) # 패딩
    nlst = []

    while len(lst)>1:
        ci,cj,cm,cs,cd = lst.pop(0)
        i = 0
        cnt = 0
        flag = True
        sm,ss = cm,cs
        while True:
            ti,tj,tm,ts,td = lst[i]
            if (ci,cj) == (ti,tj):
                cnt += 1
                sm += tm
                ss += ts
                if cd%2 != td%2:
                    flag = False
            else:
                break
            i += 1
        if cnt >= 1:
            sm = int(sm//5)
            if sm == 0:
                for _ in range(cnt):
                    lst.pop(0)
            else:
                ss = int(ss//(cnt+1))
                if flag:
                    sd = 0
                else:
                    sd = 1
                for k in range(sd,8,2):
                    nlst.append((ci,cj,sm,ss,k))
                for _ in range(cnt):
                    lst.pop(0)
        else:
            nlst.append((ci,cj,cm,cs,cd))

    lst = nlst

ans = 0
for i in range(len(lst)):
    ans += lst[i][2]
print(ans)
