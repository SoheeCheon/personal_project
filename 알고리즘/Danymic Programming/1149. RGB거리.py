from collections import deque

N = int(input())

rgb = [list(map(int, input().split())) for _ in range(N)]
result = 999999999999

def bfs(now):
    global result
    que = deque()
    que.append((0, now, rgb[0][now]))
    while que:
        house, n, n_sum = que.popleft()
        if result < n_sum:
            continue

        if house >= (N-1):
            result = n_sum
            continue

        for i in range(3):
            if n != i:
                que.append((house + 1, i, n_sum + rgb[house + 1][i]))


for a in range(3):
    bfs(a)

print(result)

