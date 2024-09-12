lst = [list(map(int,input().split())) for _ in range(4)]
arr = [[[0] * 2 for _ in range(4)] for _ in range(4)]
sdict = {}
slst = []
for i in range(1,5):
    for j in range(1,5):
        # idx
        arr[i-1][j-1][0] = lst[i-1][2*j-2]
        # dr
        arr[i-1][j-1][1] = lst[i-1][2*j-1]-1
        slst.append([arr[i-1][j-1][0],i-1,j-1,arr[i-1][j-1][1]])
        sdict[arr[i-1][j-1][0]] = [i-1,j-1,arr[i-1][j-1][1]]
slst.sort(key=lambda x:x[0])
di,dj = [-1,-1,0,1,1,1,0,-1], [0,-1,-1,-1,0,1,1,1]
ans = arr[0][0][0]
si,sj,sd = 0,0,arr[0][0][1]
is_live = [True] * 17
is_live[arr[0][0][0]] = False
arr[0][0] = [-1,-1]
while True:
    # 도둑말 이동
    for i in range(1,len(slst)+1):
        if not is_live[i]: continue
        idx,ci, cj, cd = slst[i-1]
        for k in range(8):
            ni,nj = ci+di[(cd+k)%8], cj+dj[(cd+k)%8]
            if 0 <= ni < 4 and 0<=nj<4 and arr[ni][nj][0] >= 0:
                # 다른 도둑말이 있다면 위치 변경
                if arr[ni][nj][0] > 0:
                    tmp,tdr = arr[ni][nj]
                    # 이동한 도둑말
                    slst[idx-1] = [idx,ni,nj,(cd+k)%8]
                    # 이동당한 도둑말
                    slst[tmp-1] = [tmp,ci,cj,tdr]
                    arr[ni][nj] = [idx,(cd+k)%8]
                    arr[ci][cj] = [tmp,tdr]
                elif arr[ni][nj][0] == 0:
                    slst[idx-1] = [idx,ni,nj,(cd+k)%8]
                    arr[ni][nj] = [idx, (cd + k) % 8]
                    arr[ci][cj] = [0,0] # 빈칸
                break
    # 술래말 이동
    ti,tj = si,sj
    mx,mi,mj,md = 0,si,sj,sd
    for k in range(3):
        ni,nj = ti+di[sd], tj+dj[sd]
        if 0<=ni<4 and 0<=nj<4 and arr[ni][nj][0] > 0:
            if arr[ni][nj][0] > mx:
                mx = max(mx,arr[ni][nj][0])
                mi,mj,md = ni,nj,arr[ni][nj][1]
            ti,tj = ni,nj
        else:
            break
    if mx > 0:
        si,sj,sd = mi,mj,md
        arr[si][sj] = [0,0]
        arr[mi][mj] = [-1,-1]
        ans += mx
    else:
        break

print(ans)