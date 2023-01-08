n = int(input())

# 계단의 최대 계수는 300개이기에
stair = [0] * 301
save = [0] * 301

# 계단값 저장
for i in range(n):
    stair[i] = int(input())

save[0] = stair[0]
save[1] = stair[0] + stair[1]
save[2] = max(stair[1] + stair[2], stair[0] + stair[2])

# 마지막 계단의 전 계단을 밟은 경우
# 마지막 계단의 전 계단을 밟지 않은 경우로 나뉘어서 계산한다.
for i in range(3, n):
    save[i] = max(save[i-3] + stair[i-1] + stair[i], save[i-2] + stair[i])

print(save[n-1])