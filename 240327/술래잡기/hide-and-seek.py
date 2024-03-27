N, MM, H, K = map(int,input().split())

# 도망자 좌표 입력
arr = []
for _ in range(MM):
    arr.append(list(map(int,input().split())))

# 나무 좌표 입력
tree = set()
for _ in range(H):
    i, j = map(int,input().split())
    tree.add((i,j))

# 0(좌) 1(우) 2(하) 3(상)
di = [0,0,1,-1]
dj = [-1,1,0,0]
opp = {0:1, 1:0, 2:3, 3:2}

# 상 우 하 좌 / 술래 방향(바깥으로 돌 때 방향)
tdi = [-1,0,1,0]
tdj = [0,1,0,-1]

# 달팽이 회전을 위해 필요한 변수
mx_cnt, cnt, flag, val = 1, 0, 0, 1
M = (N+1) // 2
ti, tj, td = M, M, 0
ans = 0

for k in range(1,K+1):
    # [1] 도망자의 이동(arr)
    for i in range(len(arr)):
        if abs(arr[i][0]-ti) + abs(arr[i][1]-tj) <= 3: # 거리가 3 이하인 경우
            ni, nj = arr[i][0] + di[arr[i][2]], arr[i][1] + dj[arr[i][2]]
            if 1<=ni<=N and 1<=nj<=N: # 범위안이면 술래 체크
                if (ni,nj) != (ti,tj): # 술래 위치가 아니면
                    arr[i][0], arr[i][1] = ni, nj

            else:
                nd = opp[arr[i][2]]
                ni, nj = arr[i][0] + di[nd], arr[i][1] + dj[nd]
                if (ni,nj) != (ti,tj):
                    arr[i] = [ni,nj,nd] # 방향이 바뀐채로 이동처리
    # [2] 술래의 이동
    cnt += 1
    ti, tj = ti+tdi[td], tj+tdj[td]
    if (ti,tj) == (1,1): # 안쪽으로 동작하는 달팽이
        mx_cnt, cnt, flag, val = N, 1, 1, -1
        td = 2 # 초기 방향은 아래로
    elif (ti,tj) == (M,M):
        mx_cnt,cnt,flag,val = 1,0,0,1
        td = 2
    else:
        if cnt == mx_cnt: # 방향 변경
            cnt = 0
            td = (td+val) % 4
            if flag == 0:
                flag = 1
            else:
                flag = 0 # 두 번에 한 번씩 길이 증가
                mx_cnt += val

    # [3] 도망자 잡기(술래자리 포함 3칸: 나무가 없는 도망자면 잡힘)
    tset = set(((ti,tj),(ti+tdi[td],tj+tdj[td]),(ti+tdi[td]*2,tj+tdj[td]*2)))

    # 뒤부터 삭제 (pop() 처럼)
    for i in range(len(arr)-1,-1,-1):
        if (arr[i][0], arr[i][1]) in tset and (arr[i][0],arr[i][1]) not in tree:
            arr.pop(i)
            ans += k

    if not arr:
        break

print(ans)