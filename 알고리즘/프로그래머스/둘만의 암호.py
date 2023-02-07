def solution(s, skip, index):
    answer = ''

    english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    for a in s:
        idx = english.index(a)

        shift = []
        while len(shift) < index:
            idx += 1
            idx %= 26
            if english[idx] in skip:
                continue
            else:
                shift.append(english[idx])

        answer += shift[-1]

    return answer

print(solution("aukks", "wbqd", 5))