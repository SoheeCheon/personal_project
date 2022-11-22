from collections import deque
import copy

N, M = map(int, input().split())

# arr를 string 배열로 한다.
string_arr = [input() for  _ in range(N)]
arr = []
for n in range(N):
    lst = []
    for m in range(M):
        if string_arr[n][m] == '1':
            lst.append(-1)
        else:
            lst.append(0)
    arr.append(lst)

que = deque([])

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
ans = 999999


def bfs():
    global ans
    copy_arr = copy.deepcopy(arr)
    que.append((0, 0))
    while que:
        ci, cj = que.popleft()
        for idx in range(4):
            ni = ci + di[idx]
            nj = cj + dj[idx]
            if 0 <= ni < N and 0 <= nj < M and copy_arr[ni][nj] == 0:
                copy_arr[ni][nj] = copy_arr[ci][cj] + 1
                que.append((ni, nj))

    if (copy_arr[N-1][M-1] > 0):
        ans = min(ans, copy_arr[N-1][M-1])

bfs()
for n in range(N):
    for m in range(M):
        if arr[n][m] == -1:
            arr[n][m] = 0
            bfs()
            arr[n][m] = -1

if ans == 999999:
    print(-1)
    exit(0)
print(ans+1)