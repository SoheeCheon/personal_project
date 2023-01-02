from collections import deque

N = int(input())


def bfs():
    visit = [0] * (N+1)
    que = deque()
    que.append(0)
    while que:
        now = que.popleft()

        # 결과가 나왔다면
        if now == N:
            print(visit[now])
            return

        for i in [now+3, now+5]:
            if i <= N and visit[i] == 0:
                que.append(i)
                visit[i] = visit[now] + 1

    print(-1)


bfs()
