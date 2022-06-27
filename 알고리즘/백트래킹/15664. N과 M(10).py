N, M = map(int, input().split())
numbers = list(map(int, input().split()))
idx = [0] * N

# 오름차순으로 출력
numbers.sort()


def permutation(lst,n, visit):
    global result
    if len(lst) == M:
        print(*lst)
        return

    overlap = 0
    for i in range(n, N):
        # if A in B 문으로 중복을 검사하려 했으나 값이 커질수록 연산량도 많아져 시간초과 발생
        # 이전 값을 저장하는 overlap을 이용 만약 다음값이 전값과 비슷하다면 넘기는 식으로 중복을 제거
        if not idx[i] and overlap != numbers[i]:
            visit[i] = 1
            lst.append(numbers[i])
            overlap = numbers[i]
            permutation(lst,i, visit)
            visit[i] = 0
            lst.pop()

permutation([],0,idx)