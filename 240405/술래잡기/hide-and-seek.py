N, MM, H, K = map(int,input().split())

# 방향 상 우 하 좌 (바깥으로 돌 떄 방향) 술래방향
tdi = [-1,0,1,0]
tdj = [0, 1, 0, -1]

arr = [list(map(int,input().split())) for _ in range(MM)]
tree = set()
for _ in range(H):
    i,j = map(int,input().split())
    tree.add((i,j))

# 0(좌) 1(우) 2(하) 3(상)
di = [0,0,1,-1]
dj = [-1,1,0,0]
opp = {0:1, 1:0, 2:3,3:2} # 반대 방향

mx_cnt, cnt, flag, val = 1, 0, 0, 1 # 증가 감소하는 값을 val로 설정

M = (N+1)//2
ti, tj, td = M, M, 0
tarr = [[0] * (N+2) for _ in range(N+2)]


ans = 0
for k in range(1,K+1):
    # [1] 도망자의 이동 (arr)
    for i in range(len(arr)):
        if abs(arr[i][0]-ti) + abs(arr[i][1]-tj) <= 3: #술래와 거리가 3 이하인 경우
            ni,nj = arr[i][0] + di[arr[i][2]], arr[i][1] + dj[arr[i][2]]
            if 1<=ni<=N and 1<=nj<=N: # 범위내면 술래 체크
                if (ni,nj) != (ti,tj): # 술래위치가 아니면 이동
                    arr[i][0], arr[i][1] = ni,nj
            else: # 범위 밖 => 방향 반대
                nd = opp[arr[i][2]]
                ni,nj = arr[i][0] + di[nd], arr[i][1]+dj[nd]
                if (ni,nj) != (ti,tj):
                    arr[i] = [ni,nj,nd] # 이동처리 (방향도 바뀜)

    # [2] 술래의 이동
    cnt += 1
    tarr[ti][tj] = k # 확인용(임시) 디버그용
    ti,tj = ti+tdi[td], tj+tdj[td]
    if (ti,tj) == (1,1): # 안쪽으로 동작하는 달팽이
        mx_cnt,cnt,flag, val = N,1,1,-1 # 한 칸 왔다고 생각하고 cnt = 1 flag도 한번에 바꿔야하므로 1로 설정
        td = 2 # 초기 방향은 아래로(하)

    elif (ti,tj) == (M,M): # 바깥으로 동작하는 달팽이
        mx_cnt, cnt, flag, val = 1, 0, 0, 1
        td = 0
    else:
        if cnt == mx_cnt:
            cnt = 0
            td = (td+val)%4
            if flag == 0:
                flag = 1

            else:
                flag = 0 # 두 번에 한 번씩 길이 증가
                mx_cnt += val

    # [3] 도망자 잡기 (술래자리 포함 3칸 : 나무가 없는 도망자면 잡힘) arr의 끝부터 pop
    tset = set(((ti,tj),(ti+tdi[td],tj+tdj[td]), (ti+tdi[td]*2,tj+tdj[td]*2)))

    for i in range(len(arr)-1,-1,-1): # pop을 위한
        if (arr[i][0],arr[i][1]) in tset and (arr[i][0],arr[i][1]) not in tree:
            arr.pop(i)
            ans += k
    # 도망자가 없다면 더이상 점수도 없음
    if not arr:
        break

print(ans)