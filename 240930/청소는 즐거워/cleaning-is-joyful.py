import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
pdict = {}
adict = {}
plst = [2,10,7,1,5,10,7,1,2]
for dr in range(4):
    if dr == 0:
        pdict[dr] = [(-2,0),(-1,-1),(-1,0),(-1,1),(0,-2),(1,-1),(1,0),(1,1),(2,0)]
    elif dr == 1:
        pdict[dr] = [(0,-2),(1,-1),(0,-1),(-1,-1),(2,0),(1,1),(0,1),(-1,1),(0,2)]
    elif dr == 2:
        pdict[dr] = [(-2,0),(-1,1),(-1,0),(-1,-1),(0,2),(1,1),(1,0),(1,-1),(2,0)]
    else:
        pdict[dr] = [(0, -2), (-1, -1), (0, -1), (1, -1), (-2, 0), (-1, 1), (0, 1), (1, 1), (0, 2)]

for dr in range(4):
    if dr == 0:
        adict[dr] = (0,-1)
    elif dr == 1:
        adict[dr] = (1,0)
    elif dr == 2:
        adict[dr] = (0,1)
    else:
        adict[dr] = (-1,0)

ci,cj,cd = N//2, N//2,0
tdi,tdj = [0,1,0,-1],[-1,0,1,0]
mx_cnt,cnt,flag = 1,0,0
ans = 0
for turn in range(1,N*N):

    # 1. 나선형 이동

    ci,cj = ci+tdi[cd], cj+tdj[cd]
    cnt += 1

    # 2. 청소 시작(비율대로 계산)
    dlst = pdict[cd]
    adi, adj = adict[cd]
    tmp = 0
    for i in range(len(dlst)):
        di,dj = dlst[i]
        mul = plst[i] * 0.01
        ni,nj = ci+di,cj+dj
        if 0<=ni<N and 0<=nj<N:
            arr[ni][nj] = arr[ni][nj] + int(arr[ci][cj] * mul)
            tmp += int(arr[ci][cj] * mul)
        else:
            ans += int(arr[ci][cj] * mul)
            tmp += int(arr[ci][cj] * mul)
    # 알파 처리
    ni,nj = ci+adi,cj+adj
    a = arr[ci][cj] - tmp
    if 0<=ni<N and 0<=nj<N:
        arr[ni][nj] = arr[ni][nj] + a
    else:
        ans += a
    arr[ci][cj] = 0

    if mx_cnt == cnt:
        cnt = 0
        cd = (cd+1)%4

        if flag:
            mx_cnt += 1
            flag = False
        else:
            flag = True
print(ans)