T = int(input())

for _ in range(T):
    N = int(input())

    # 초기값 구성, 인덱스를 맞추기 위해서 0번째를 채워준다.
    lst = [0, 1, 1, 1]

    for i in range(4, N + 1):
        lst.append(lst[i-3] + lst[i-2])

    print(lst[N])