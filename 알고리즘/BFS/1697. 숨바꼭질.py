from collections import deque

N, K = map(int, input().split())


def bfs():
    que = deque()
    que.append(N)
    visit = [0] * 100001
    while que:
        now = que.popleft()

        if now == K:
            print(visit[K])
            return


        for i in [now +1, now -1, 2 * now]:
            if 0 <= i <= 100000 and visit[i] == 0:
                visit[i] = visit[now] + 1
                que.append(i)

    return


bfs()