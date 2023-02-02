import heapq


def solution(n, k, enemy):
    if k >= len(enemy): return len(enemy)

    heap = []

    # k번째 까지는 무조건 가므로
    for e in enemy[:k]:
        heapq.heappush(heap, e)

    for i in range(k, len(enemy)):
        heapq.heappush(heap, enemy[i])
        n -= heapq.heappop(heap)

        if n < 0: return i

    return len(enemy)
