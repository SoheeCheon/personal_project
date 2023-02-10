# ["aya", "ye", "woo", "ma"] => 4가지 발음 & 조합해서 할 수 있는 발음
# 연속한 발음은 x
# babbling 중 조카가 발음할 수 있는 것을 return
def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]

    for bab in babbling:
        if bab in can:
            answer += 1
        else:
            word = ""
            s, e = 0, 2
            while e <= len(bab):
                if e - s == 2 and bab[s:e] != word:
                    if bab[s:e] == "ye" or bab[s:e] == "ma":
                        word = bab[s:e]
                        s = e
                        e += 2
                    else:
                        e += 1
                elif e - s == 3 and bab[s:e] != word:
                    if bab[s:e] == "aya" or bab[s:e] == "woo":
                        word = bab[s:e]
                        s = e
                        e += 2
                    else:
                        break
                else:
                    break

            if len(bab) + 2 == e:
                answer += 1

    return answer

print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))