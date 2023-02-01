def solution(n, l, r):
    def count_bit(num):
        if num <= 5: return "11011"[:num].count("1")

        base = 1
        while 5 ** (base + 1) < num:
            base += 1

        section = num // (5 ** base)
        remainder = num % (5 ** base)

        answer = section * (4 ** base)

        # 3이상이면 중간에 0인 구간이 끼어있기 때문에 값을 추가적으로 더해진 값 제거
        if section >= 3:
            answer -= 4 ** base

        if section == 2:
            return answer
        else:
            return count_bit(remainder) + answer

    return count_bit(r) - count_bit(l - 1)