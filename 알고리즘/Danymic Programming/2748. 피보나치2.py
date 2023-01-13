N = int(input())

# 1, 2, 3의 초깃값을 넣어둔다.
fibo = [0, 1, 1]

for i in range(3, N+1):
    fibo.append(fibo[i-2] + fibo[i-1])

print(fibo[N])