from collections import deque

S, E = map(int, input().split())

# 여기에 거리를 저장한다.
visit = [0] * 100001
check = [False] * 100001


def bfs():
    que = deque([])
    que.append(S)
    while que:
        now = que.popleft()
        if now == E:
            return visit[now]

        if 0 <= now * 2 <= 100000 and check[now*2] == False:
            que.append(now*2)
            visit[now*2] = visit[now]
            check[now*2] = True

        if now - 1 >= 0 and  check[now-1] == False:
            que.append(now-1)
            visit[now-1] = visit[now] + 1
            check[now-1] = True

        if now + 1 <= 100000 and check[now+1] == False:
            que.append(now + 1)
            visit[now + 1] = visit[now] + 1
            check[now+1] = True



print(bfs())