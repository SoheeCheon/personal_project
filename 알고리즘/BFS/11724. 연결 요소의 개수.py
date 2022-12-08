from collections import deque
# 노드의 갯수, 간선의 갯수
N, M = map(int, input().split())

# 그래프를 저장할 공간
arr = [[0] * (N+1) for _ in range(N+1)]
# 간선의 정보를 저장할 공간
lst = [0] * (N+1)

# 그래프를 연결함
for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1


def bfs(now, time):
    que = deque([now])
    lst[now] = time
    while que:
        n = que.popleft()
        for i in range(1, N+1):
            if arr[n][i] == 1 and lst[i] == 0:
                lst[i] = time
                que.append(i)


cnt = 1
for i in range(1, N+1):
    if lst[i] == 0:
        bfs(i, cnt)
        cnt += 1

print(cnt - 1)