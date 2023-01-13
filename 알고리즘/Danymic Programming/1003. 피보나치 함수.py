T = int(input())

for _ in range(T):
    N = int(input())

    fibo = [0, 1, 1]
    # 이중 리스트로 만들어 0과 1이 호출된 횟수를 저장한다.
    count = [[1, 0], [0, 1], [1, 1]]

    # 피보나치 수열과 0과 1인 갯수
    for i in range(3, N+1):
        fibo.append(fibo[i-2] + fibo[i-1])
        count.append([count[i-2][0] + count[i-1][0], count[i-2][1] + count[i-1][1]])

    print(count[N][0], end=" ")
    print(count[N][1])