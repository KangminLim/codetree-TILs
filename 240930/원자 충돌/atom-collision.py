N, M, K = map(int,input().split())
tlst = []
di,dj = [-1,-1,0,1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1]
for _ in range(M):
    x,y,m,s,d = map(int,input().split())
    tlst.append((x-1,y-1,m,s,d))
for turn in range(1,K+1):
    # 1. 모든 원자 이동
    for i in range(len(tlst)):
        ci,cj,cm,cs,cd = tlst[i]
        ni,nj = (ci+di[cd]*cs)%N,(cj+dj[cd]*cs)%N
        tlst[i] = (ni,nj,cm,cs,cd)

    nlst = []
    tlst.sort(key=lambda x:(x[0],x[1]))
    tlst.append((100,100,10000,10000,8)) # 패딩
    # print('')
    # 2. 원자 합성 진행
    while len(tlst) > 1:
        ci,cj,cm,cs,cd = tlst.pop(0)
        i = 0
        cnt = 0
        flag = True
        sm,ss = cm,cs
        while True:
            ti,tj,tm,ts,td = tlst[i]
            if (ci,cj) == (ti,tj):
                cnt += 1
                sm += tm
                ss += ts
                if cd%2 != td%2:
                    flag = False
            else:
                break
            i += 1
        # 원소 합성 진행
        if cnt >= 1:
            sm = int(sm//5)
            if sm ==0:
                for _ in range(cnt):
                    tlst.pop(0)
                continue
            ss = int(ss//(cnt+1))
            if flag:
                sd = 0
            else:
                sd = 1
            for k in range(sd,8,2):
                nlst.append((ci,cj,sm,ss,k))
            for _ in range(cnt):
                tlst.pop(0)
        else:
            nlst.append((ci,cj,cm,cs,cd))
    # print('')

    tlst = nlst

ans = 0
for i in range(len(tlst)):
    ans += tlst[i][2]
print(ans)