n = int(input())

arr = [0, 1, 2]
# 피보나치 수열을 따르고 있다.
for i in range(3, n+1):
    arr.append(arr[i - 2] + arr[i - 1])

print(arr[n] % 10007)
