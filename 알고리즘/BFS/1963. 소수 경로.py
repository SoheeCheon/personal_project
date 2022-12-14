from collections import deque

T = int(input())

odd = [0] * 10001
for i in range(2, 101):
    if odd[i] == 0:
        j = i * 2
        while j < 10001:
            odd[j] = 1
            j += i


for _ in range(T):

    def bfs():
        que = deque()
        que.append(A)
        visit = [0] * 10001
        visit[A] = 1
        while que:
            now = que.popleft()

            if now == B:
                print(visit[now]-1)
                return

            if now < 1000: continue

            for i in [1, 10, 100, 1000]:
                next = now - now % (i * 10) // i * i

                for _ in range(10):
                    if visit[next] == 0 and odd[next] == 0:
                        visit[next] = visit[now] + 1
                        que.append(next)
                    next += i

        print('Impossible')
        return


    A, B = map(int, input().split())
    bfs()


