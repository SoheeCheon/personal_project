from collections import deque

X = int(input())


def bfs():
    visit = [0] * (X + 1)
    que = deque()
    que.append(X)
    while que:
        now = que.popleft()

        if now == 1:
            print(visit[now])
            return

        if now % 3 == 0 and visit[now//3] == 0:
            que.append(now//3)
            visit[now//3] = visit[now] + 1

        if now % 2 == 0 and visit[now//2] == 0:
            que.append(now//2)
            visit[now//2] = visit[now] + 1

        if visit[now-1] == 0:
            que.append(now-1)
            visit[now-1] = visit[now] + 1


bfs()