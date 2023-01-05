from collections import deque

n = int(input())
stair = [0]
for _ in range(n):
    stair.append(int(input()))

# 각 계단에 대한 최대값이 들어갈 배열
max_stair = [0] * (n + 1)

def bfs():
    global max_stair, stair
    que = deque()
    # 현재 위치, 연속된 1의 갯수, 합이 que에 저장되있다.
    que.append((0, 0, 0))
    while que:
        now, cnt1, ssum = que.popleft()
        if max_stair[now] < ssum:
            max_stair[now] = ssum

        for i in range(1, 3):
            # 범위안에 있을 때
           if now + i <= n:
                if i == 1 and cnt1 < 2:
                    que.append((now+i, cnt1 + 1, ssum + stair[now+i]))

                elif i == 2:
                    que.append((now+i, 1, ssum + stair[now+i]))

bfs()
print(max_stair[n])


