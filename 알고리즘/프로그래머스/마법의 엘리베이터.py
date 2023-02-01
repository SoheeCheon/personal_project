def solution(storey):
    answer = 0

    # 값이 0이 될때까지 반복
    while storey != 0:
        # 일의 자리부터 차례대로 층을 바꾼다.
        num = storey % 10

        # 6이상이면 무조건 오르는게 시간이 덜 걸리므로 더한다
        if num >= 6:
            answer += 10 - num
            storey += 10

        # 5이고 다음 자리 층수가 5이상이면 위로 올라간다
        elif num == 5 and (storey // 10) % 10 >= 5:
            answer += 10 - num
            storey += 10

        # 이 모든 경우가 아닐 때 내려간다.
        else:
            answer += num

        storey //= 10

    return answer