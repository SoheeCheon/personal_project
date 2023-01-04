from collections import deque

N = int(input())

rgb = [list(map(int, input().split())) for _ in range(N)]
result = 999999999999

def bfs(now):
    global result
    que = deque()
    que.append((now, rgb[0][now]))
    house_num = 1
    while que:
        n, n_sum = que.popleft()

        if result < n_sum:
            return

        if house_num >= N:
            result = n_sum
            return

        for i in range(3):
            if n != i:
                que.append((i, n_sum + rgb[house_num][i]))
        house_num += 1

for a in range(3):
    bfs(a)
print(result)

