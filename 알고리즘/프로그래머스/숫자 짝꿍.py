# 같은 숫자로 만들 수 있는 가장 큰 수
# X, Y 숫자 갯수를 저장할 리스트와 공통된 숫자를 저장할 리스트를 만든다.
# X, Y의 숫자 갯수를 세고 두 값 중 작은 값으로 answer에 추가한다.

# for문으로 하나씩 갯수를 세어 저장하려 했으나 시간초과로 인해 Counter를 사용

from collections import Counter


def solution(X, Y):
    answer = ''

    countx = Counter(X)
    county = Counter(Y)

    for idx in range(9, -1, -1):
        cnt = min(countx[str(idx)], county[str(idx)])
        answer += (str(idx) * cnt)

    # 마지막에 형변환을 사용하였더니 그것으로 시간초과가 발생하여
    # 조건으로 return 값을 배정
    if len(answer) == 0:
        return "-1"
    if answer[0] == "0":
        return "0"
    return answer