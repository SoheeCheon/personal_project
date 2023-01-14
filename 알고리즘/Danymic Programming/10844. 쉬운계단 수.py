N = int(input())

fibo = [0, 9, 17]

for n in range(3, N+1):
    fibo.append(fibo[n-1]*2 -1)

print(fibo[N])
