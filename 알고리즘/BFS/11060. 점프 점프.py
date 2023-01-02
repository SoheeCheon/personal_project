from collections import deque

N = int(input())
lst = list(map(int, input().split()))
visit = [0] * N


def bfs():
    que = deque()
    que.append(0)
    visit[0] = 1
    while que:
        now = que.popleft()
        if now == (N - 1):
            print(visit[now] - 1)
            return

        # lst에 적혀있는 숫자를 통해 갈수 있는 만큼 이동함
        for i in range(1, lst[now] + 1):
            next = now + i
            if 0 <=  next < N and visit[next] == 0:
                que.append(next)
                visit[next] = visit[now] + 1

    print(-1)
    return


bfs()
