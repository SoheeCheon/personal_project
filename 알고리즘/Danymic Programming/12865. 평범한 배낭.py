N, K = map(int, input().split())

# 물건들의 정보
weight = []
value = []
for _ in range(N):
    a, b = map(int, input().split())
    weight.append(a)
    value.append(b)

lst = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        # j가 무게보다 작으면 이전 값을 덮어씌운다.
        if j < weight[i]:
            lst[i][j] = lst[i-1][j]
        # 무게보다 커지면 이전 값과 현재값을 더한 것과, 이전값을 비교해 큰 값을 저장한다.
        else:
            lst[i][j] = max(value[i] + lst[i-1][j-weight[i]], lst[i-1][j])

print(lst[N-1][K])
