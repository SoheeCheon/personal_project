N, money = map(int, input().split())

coins = list(int(input()) for _ in range(N))

# 동전의 갯수를 셀 변수
cnt = 0
# 큰 동전부터 차례대로
for i in range(N-1, -1, -1):

    if money == 0:
        break

    if money < coins[i]:
        continue

    cnt += money // coins[i]
    money %= coins[i]


print(cnt)