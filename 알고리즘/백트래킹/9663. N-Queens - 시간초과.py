N = int(input())

arr = [0] * N
cnt = 0


def processing(idx):
    for num in range(idx):
        # 같은 열에 존재하거나 위쪽 대각선에만 존재하지 않으면 됨
        if arr[idx] == arr[num] or abs(arr[idx] - arr[num]) == abs(idx - num):
            return False

    return True


def find(n):
    global cnt

    if n == N:
        cnt += 1
        return

    for i in range(N):
        arr[n] = i
        if processing(n):
            find(n+1)


find(0)
print(cnt)