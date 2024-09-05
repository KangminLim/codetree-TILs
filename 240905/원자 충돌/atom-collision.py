N, M, K = map(int,input().split())
alst = [list(map(int,input().split())) for _ in range(M)]

di,dj = [-1,-1,0,1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1]

for _ in range(K):
    #  1. 모든 파이어볼 이동
    tlst = []
    for i in range(len(alst)):
        ci,cj,cm,cs,cd = alst[i]
        ni,nj = (ci+di[cd]*cs)%N, (cj+dj[cd]*cs)%N
        tlst.append([ni,nj,cm,cs,cd])
    tlst.sort(key = lambda x:(x[0],x[1]))
    # while문을 위한 패딩
    tlst.append([100,100,0,0,0])
    i = 0
    tmp = []
    while i < len(tlst)-1:
        si,sj,sm,ss,sd = tlst[i]
        start_dr = 0
        for j in range(i+1,len(tlst)):
            ci, cj, cm, cs, cd = tlst[j]

            if (si,sj) == (ci,cj): # 같은 좌표에 있으면 합침
                sm += cm
                ss += cs

                if (sd%2) != (cd%2):
                    start_dr = 1
            else:
                if j-i == 1: # 1개면 그냥 추가
                    tmp.append(tlst[i])
                elif sm // 5 >= 1:
                    for dr in range(start_dr,8,2):
                        tmp.append([si,sj,sm//5,ss//(j-i),dr])
                break
        i = j
    alst = tmp

ans = 0
for a in alst:
    ans += a[2]
print(ans)