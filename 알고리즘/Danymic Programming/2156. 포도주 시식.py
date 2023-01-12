N = int(input())

wine = [int(input()) for _ in range(N)]
save = [0] * N

# 초기값 지정
save[0] = wine[0]
save[1] = wine[1] + wine[0]
save[2] = max(wine[1] + wine[2], wine[0] + wine[2])

# 다음값 계속 지정
for i in range(3, N):
    save[i] = max(save[i-3] + wine[i-1] + wine[i], save[i-2] + wine[i])

# 최대값 출력
print(max(save))

