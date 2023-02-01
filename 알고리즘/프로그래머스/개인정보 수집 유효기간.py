def solution(today, terms, privacies):
    answer = []
    today_year = int(today[:4])
    today_month = int(today[5:7])
    today_day = int(today[8:])

    # 기간 정보가 담긴 딕셔너리
    dic = dict()
    for str in terms:
        dic[str[0]] = int(str[2:])

    idx = 0
    for privarcy in privacies:
        idx += 1
        type = privarcy[-1]
        pri_year = int(privarcy[:4])
        pri_month = int(privarcy[5:7])
        pri_day = int(privarcy[8:10])

        pri_month += dic[type]

        # 넘어가는 년도를 계산
        while pri_month >= 13:
            pri_year += 1
            pri_month -= 12

        # 이전 조건을 중첩에서 작성
        if pri_year < today_year:
            answer.append(idx)
            continue
        elif pri_year == today_year and pri_month < today_month:
            answer.append(idx)
            continue
        elif pri_year == today_year and pri_month == today_month and pri_day <= today_day:
            answer.append(idx)
            continue

    return answer