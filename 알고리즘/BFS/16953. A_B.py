from collections import deque

A, B = map(int, input().split())


def bfs():
    que = deque([])
    que.append((1, B))

    while que:
        n, now = que.popleft()
        if now == A:
            print(n)
            return

        if now % 2 == 0:
            now2 = now // 2
            if now2 >= A:
                que.append((n+1, now2))

        if now % 10 == 1:
            now_right_1 = now // 10
            if now_right_1 >= A:
                que.append((n+1, now_right_1))

    print(-1)
    return


bfs()