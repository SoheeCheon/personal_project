N = int(input())

rgb = [list(map(int, input().split())) for _ in range(N)]

for n in range(1, N):
    rgb[n][0] += min(rgb[n - 1][1], rgb[n - 1][2])
    rgb[n][1] += min(rgb[n - 1][0], rgb[n - 1][2])
    rgb[n][2] += min(rgb[n - 1][1], rgb[n - 1][0])

print(min(rgb[N-1][0], rgb[N-1][1], rgb[N-1][2]))
