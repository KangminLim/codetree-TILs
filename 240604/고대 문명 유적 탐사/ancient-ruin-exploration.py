from collections import deque

# 회전 함수
def rotate90(arr, si, sj):
    narr = [row[:] for row in arr]
    for i in range(3):
        for j in range(3):
            narr[si + i][sj + j] = arr[si + 2 - j][sj + i]
    return narr

def rotate180(arr, si, sj):
    narr = [row[:] for row in arr]
    for i in range(3):
        for j in range(3):
            narr[si + i][sj + j] = arr[si + 2 - i][sj + 2 - j]
    return narr

def rotate270(arr, si, sj):
    narr = [row[:] for row in arr]
    for i in range(3):
        for j in range(3):
            narr[si + i][sj + j] = arr[si + j][sj + 2 - i]
    return narr

# 유물 탐색 및 획득 함수
def bfs(si, sj, arr, v):
    q = deque()
    q.append((si, sj))
    v[si][sj] = True
    group = {(si, sj)}
    cnt = 1
    while q:
        ci, cj = q.popleft()
        for ni, nj in ((ci - 1, cj), (ci + 1, cj), (ci, cj - 1), (ci, cj + 1)):
            if 0 <= ni < 5 and 0 <= nj < 5 and not v[ni][nj] and arr[si][sj] == arr[ni][nj]:
                q.append((ni, nj))
                group.add((ni, nj))
                v[ni][nj] = True
                cnt += 1
    if cnt >= 3:
        return cnt, group
    else:
        return 0, set()

# 탐사 및 유물 획득
def simulate_rotation(arr, rotation_fn):
    mx = 0
    best_arr = []
    best_group = set()
    for i in range(3):
        for j in range(3):
            rotated_arr = rotation_fn(arr, i, j)
            current_sum = 0
            visited = [[False] * 5 for _ in range(5)]
            groups = []
            for ci in range(5):
                for cj in range(5):
                    if not visited[ci][cj]:
                        count, group = bfs(ci, cj, rotated_arr, visited)
                        if count > 0:
                            current_sum += count
                            groups.append(group)
            if current_sum > mx:
                mx = current_sum
                best_arr = rotated_arr
                best_group = set().union(*groups)
    return best_arr, mx, best_group

def fill_new_artifacts(arr, tq):
    empty_positions = [(i, j) for j in range(5) for i in range(4, -1, -1) if arr[i][j] == 0]
    for i, j in empty_positions:
        arr[i][j] = tq.popleft()

def simulate(arr):
    max_sum = 0
    total_sum = 0
    best_group = set()
    visited = [[False] * 5 for _ in range(5)]
    for ci in range(5):
        for cj in range(5):
            if not visited[ci][cj]:
                count, group = bfs(ci, cj, arr, visited)
                if count > 0:
                    total_sum += count
                    best_group.update(group)
    return total_sum, best_group

# 메인 로직
def main():
    K, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(5)]
    tlst = list(map(int, input().split()))
    tq = deque(tlst)

    answers = []
    for _ in range(K):
        arr90, sum90, group90 = simulate_rotation(arr, rotate90)
        arr180, sum180, group180 = simulate_rotation(arr, rotate180)
        arr270, sum270, group270 = simulate_rotation(arr, rotate270)

        if sum90 == 0 and sum180 == 0 and sum270 == 0:
            break

        if sum90 >= max(sum180, sum270):
            arr = arr90
            target_group = group90
            max_sum = sum90
        elif sum180 >= sum270 and sum180 > sum90:
            arr = arr180
            target_group = group180
            max_sum = sum180
        else:
            arr = arr270
            target_group = group270
            max_sum = sum270

        while True:
            target_group = sorted(target_group, key=lambda x: (x[1], -x[0]))
            for ci, cj in target_group:
                arr[ci][cj] = 0
            fill_new_artifacts(arr, tq)
            new_sum, new_group = simulate(arr)
            if new_sum == 0:
                break
            max_sum += new_sum
            target_group = new_group

        answers.append(max_sum)

    print(" ".join(map(str, answers)))

if __name__ == "__main__":
    main()