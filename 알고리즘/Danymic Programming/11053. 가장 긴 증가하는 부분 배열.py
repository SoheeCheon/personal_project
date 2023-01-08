N = int(input())
lst = list(map(int, input().split()))

# 최소 숫자와 최대거리를 갱신
min_num = min(lst)
max_dis = [1] * N

for n in range(N):
    # 현재 인덱스가 최소 리스트라면 넘긴다.
    if lst[n] == min_num:
        continue

    max_idx = 0
    for i in range(n):
        if lst[n] > lst[i]:
            max_dis[n] = max(max_dis[i] + 1, max_dis[n])

print(max(max_dis))





