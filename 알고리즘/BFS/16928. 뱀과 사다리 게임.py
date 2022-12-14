from collections import deque

N, M = map(int, input().split())

arr = [0] * 101
lst = [0] * (N+M+1)
visit = [0] * 101

# 사다리 정보와 뱀의 정보
for i in range(1, N+M+1):
    s, e = map(int, input().split())

    arr[s] = i
    lst[i] = e


def bfs():
    que = deque([])
    que.append(1)
    visit[1] = 0
    while que:
        now = que.popleft()

        if now == 100:
            print(visit[100])
            return

        for i in range(1, 7):
            next = now + i
            if 0 <= next <= 100 and visit[next] == 0:
                if arr[next] == 0:
                    visit[next] = visit[now] + 1
                    que.append(next)
                else:
                    goal = lst[arr[next]]
                    if visit[goal] == 0:
                        visit[goal] = visit[now] + 1
                        que.append(goal)


bfs()



