N = int(input())

# 삼각형의 정보
triangle = [list(map(int, input().split())) for _ in range(N)]
# 최대값을 저장하는 배열
max_tri = [[0] * i for i in range(1, N+1)]
max_tri[0][0] = triangle[0][0]

for n in range(N-1):
    # 다음 트리의 합계를 구하는 for문
    for i in range(n+1):
        max_tri[n + 1][i] = max(max_tri[n][i] + triangle[n + 1][i], max_tri[n + 1][i])
        max_tri[n + 1][i + 1] = max(max_tri[n][i] + triangle[n + 1][i + 1], max_tri[n + 1][i + 1])

print(max(max_tri[N-1]))
