N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visit = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(v):
    queue = [v]
    visit[v] = 1

    while queue:
        now = queue.pop(0)

        if graph[now]:
            for idx in graph[now]:
                if visit[idx] == 0:
                    visit[idx] = 1
                    queue.append(idx)


cnt = 0
for i in range(1, N+1):
    if visit[i] == 0:
        if not graph[i]:
            bfs(i)
            cnt += 1
        else:
            cnt += 1
            visit[i] = 1


print(cnt)