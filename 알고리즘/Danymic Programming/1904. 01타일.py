N = int(input())

lst = [0, 1, 2, 3, 5, 8]

for i in range(6, N+1):
    lst.append((lst[i-2] + lst[i-1]) % 15746)

print(lst[N])