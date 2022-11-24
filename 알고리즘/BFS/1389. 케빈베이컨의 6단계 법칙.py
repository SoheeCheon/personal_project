from collections import deque

N, M = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
bacon = [0] * (N+1)
ans = 99999999
# graph 로 친구 연결
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b], graph[b][a] = 1, 1


def bfs(start):
    que = deque([])
    visit = [0] * (N+1)
    que.append(start)
    while que:
        now = que.popleft()
        for i in range(1, N+1):
            # 친구관계가 연결되어있고 방문하지 않은 친구만
            if graph[now][i] == 1 and visit[i] == 0 and i != start:
                visit[i] = visit[now] + 1
                que.append(i)

    return visit


for num in range(1, N + 1):
    total = bfs(num)
    bacon[num] = sum(total)
    # 최소값 갱신
    ans = min(ans, bacon[num])

print(bacon.index(ans))
