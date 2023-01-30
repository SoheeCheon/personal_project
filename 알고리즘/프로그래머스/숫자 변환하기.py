from collections import deque


def solution(x, y, n):
    lst = [0] * (y + 1)
    que = deque()
    que.append((x, 0))

    # 바로 정답인 경우
    if x == y:
        return 0

    # 목표값에 도달했거나 도달하지 못했을 때 종료
    while lst[y] or que:
        num, time = que.popleft()
        if num == y:
            break

        # 3가지 경우의 수를 검사한다.
        for next in [num + n, 2 * num, 3 * num]:
            if next <= y and lst[next] == 0:
                lst[next] = time + 1
                que.append((next, time + 1))

    return lst[y] if lst[y] else -1