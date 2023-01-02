T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    arr = [[0] * n for _ in range(k+1)]

    # 0층의 초기 설정을 해준다.
    for num in range(1, n+1):
        arr[0][num-1] = num

    for floor in range(1, k+1):
        for detail in range(n):
            # 이전 층의 호수를 더해서 인원수를 맞춘다.
            arr[floor][detail] = sum(arr[floor-1][:detail+1])

    print(arr[k][n-1])