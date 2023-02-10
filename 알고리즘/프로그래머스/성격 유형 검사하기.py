# 왼쪽이 1 ~ 3, 오른쪽이 5 ~ 7
# 성격유형은 "RT", "CF", "JM", "AN" 이다
# 4를 기준으로 점수를 계산한다. 음수가 나오면 비동의, 양수가 나오면 동의로 계산한다.
# 4가지의 성격점수를 리스트로 만들어 계산한다.
def solution(survey, choices):
    answer = ''
    lst = [[0, 0], [0, 0], [0, 0], [0, 0]]

    cnt = len(survey)

    for idx in range(cnt):
        score = choices[idx] - 4
        if score > 0:
            type = survey[idx][1]
            if type == "R":
                lst[0][0] += score
            elif type == "T":
                lst[0][1] += score
            elif type == "C":
                lst[1][0] += score
            elif type == "F":
                lst[1][1] += score
            elif type == "J":
                lst[2][0] += score
            elif type == "M":
                lst[2][1] += score
            elif type == "A":
                lst[3][0] += score
            elif type == "N":
                lst[3][1] += score
        else:
            type = survey[idx][0]
            score = -score
            if type == "R":
                lst[0][0] += score
            elif type == "T":
                lst[0][1] += score
            elif type == "C":
                lst[1][0] += score
            elif type == "F":
                lst[1][1] += score
            elif type == "J":
                lst[2][0] += score
            elif type == "M":
                lst[2][1] += score
            elif type == "A":
                lst[3][0] += score
            elif type == "N":
                lst[3][1] += score

    word = ["RT", "CF", "JM", "AN"]
    for idx in range(4):
        if lst[idx][0] >= lst[idx][1]:
            answer += word[idx][0]
        else:
            answer += word[idx][1]
    return answer