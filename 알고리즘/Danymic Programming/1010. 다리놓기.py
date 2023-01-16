T = int(input())

for _ in range(T):
    # 왼쪽, 오른쪽의 사이트 갯수
    N, M = map(int, input().split())

    ssum = 0
    result = 0
    for i in range(1, M-N+2):
        ssum += i
        result += ssum

    print(result)
