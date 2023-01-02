from collections import deque

T = int(input())

for _ in range(T):
    N = int(input())
    visit = [0] * (N+1)


    def bfs():
        que = deque()
        que.append(0)
        while que:
            now = que.popleft()

            if now + 1 <= N:
                que.append(now+1)
                visit[now+1] += 1

            if now + 2 <= N:
                que.append(now + 2)
                visit[now + 2] += 1

            if now + 3 <= N:
                que.append(now + 3)
                visit[now + 3] += 1


        print(visit[N])
        return


    bfs()