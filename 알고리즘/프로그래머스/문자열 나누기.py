def solution(s):
    answer = 0

    N = len(s)
    i = 0
    while i < N:
        if i == N - 1:
            return answer + 1

        same, other = 1, 0
        j = i + 1
        while j < N:
            if s[i] == s[j]:
                same += 1
            else:
                other += 1

            if same == other:
                answer += 1
                i = j + 1
                break

            j += 1

        # 숫자가 하나만 연속해서 나와서 걸리지 않을 경우의 예외 처리
        if j == N:
            return answer + 1

    return answer

print(solution("abracadabra"))