N = int(input())

fibo = [0, 1, 3]

for n in range(3, N+1):
    fibo.append(fibo[n-2]*2 + fibo[n-1])

print(fibo[N])
