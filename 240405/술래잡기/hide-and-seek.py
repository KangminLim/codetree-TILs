N,M,H,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(M)] # 도망자의 lst

tree = set()

for _ in range(H):
    x,y = map(int,input().split())
    tree.add((x,y))

# 술래의 이동
tdi, tdj = [-1,0,1,0], [0,1,0,-1]

di, dj = [0,0,-1,1], [-1,1,0,0]
opp = {0:1,1:0,2:3,3:2}

tM = (N+1)//2
ti,tj,td = tM,tM,0

mx_cnt, cnt, flag, val = 1,0,0,0
ans = 0
# K턴 동안 진행
for k in range(1,K+1):
    # [1] 도망자의 움직임 (동시 이동)
    for i in range(len(arr)):
        if abs(arr[i][0]-ti) + abs(arr[i][1]-tj) <= 3: # 술래와의 거리가 3 이하라면 이동
            ni,nj = arr[i][0] + di[arr[i][2]], arr[i][1] + dj[arr[i][2]]
            if 1<=ni<=N and 1<=nj<=N: # 범위 안
                if (ni,nj) != (ti,tj): # 술래가 없다면
                    arr[i][0], arr[i][1] = ti,tj # 도망자 이동
            else: # 범위 밖, 반대로 이동
                nd = opp[arr[i][2]]
                ni,nj = arr[i][0] + di[nd], arr[i][1] + dj[nd]
                if (ni,nj) != (ti,tj):
                    arr[i] = [ni,nj,nd]


    # [2] 술래의 움직임
    cnt += 1
    ti, tj = ti + tdi[td], tj + tdj[td]

    if (ti,tj) == (1,1):
        mx_cnt, cnt, flag, val = N, 1, 1, -1
        td = 2

    elif (ti,tj) == (tM,tM):
        mx_cnt, cnt, flag, val = 1, 0, 0, 0
        td = 0

    else:
        if mx_cnt == cnt:
            cnt = 0
            td = (td+val)%4
            if flag == 0:
                flag = 1
            else:
                flag = 0
                mx_cnt += val


    # [3] 술래의 잡기 시작
    tset = set(((ti,tj),(ti+tdi[td],tj+tdj[td]),(ti+tdi[td]*2,tj+tdj[td]*2)))

    for i in range(len(arr)-1,-1,-1): # 맨 뒤부터 찾아서 삭제
        if (arr[i][0],arr[i][1]) in tset and (arr[i][0],arr[i][1]) not in tree:
            arr.pop()
            ans += k

print(ans)