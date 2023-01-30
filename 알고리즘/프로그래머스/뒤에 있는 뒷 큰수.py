def solution(numbers):
    N = len(numbers)

    # 값을 갱신할 인덱스를 담아놓는 리스트
    stack = []
    answer = [0] * N

    for i in range(N):
        # stack에 들어있는 인덱스 값보다 현재값이 크다면 answer 갱신
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        # 현재의 인덱스를 넣어준다.
        stack.append(i)

    # 마지막까지 값이 없다면 -1로 넣어준다.
    while stack:
        answer[stack.pop()] = -1

    return answer