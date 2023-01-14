N = int(input())

fibo = [0, 1, 1]

for n in range(3, N+1):
    fibo.append(fibo[n-1] + fibo[n-2])

print(fibo[N])