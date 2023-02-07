# 1. 지원자가 회사를 넣는다.
# 2. 회사는 지원자를 선택한다.
# 3. 거절된 지원자는 회사를 다시 넣는다 (1번으로)

company_select = {}
aplicant_info = {}

def solution(compaines, aplicants):
    global company_select, aplicant_info
    answer = []
    reject = []

    cnt_com = len(compaines)
    cnt_apply = len(aplicants)

    # 회사가 선택한 지원자 정보 {"A": ["a", "b"], ...}
    for c in compaines:
        company_select[c[0]] = []

    # 지원자의 회사 정보 {"a": ["A"], "b": ["C", "A", "B"], ...}
    for aplicant in aplicants:
        like_com = [aplicant[2], aplicant[3], aplicant[4]]
        aplicant_info[aplicant[0]] = like_com[:int(aplicant[-1])]
        reject.append(aplicant[0])

    def put(reject):
        global company_select, aplicant_info

        # 지원자의 회사가 남아있으면 해당 회사에 지원자를 넣어준다.
        for person in reject:
            if len(aplicant_info[person]):
                company_select[aplicant_info[person].pop(0)].append(person)


    def match(compaines, cnt_com, cnt_apply):
        global company_select, aplicant_info
        for i in range(cnt_com):
            # 선호하는 지원자 순위 : "fabdec"
            like = compaines[i][2: 2+cnt_apply]
            limit = int(compaines[i][-1])

            # ["a", "c"...]
            com_apply_people = company_select[compaines[i][0]]
            # 지원자의 수가 한계를 넘었다면 제거한다.
            if len(com_apply_people) > limit:
                save = []
                for apply_num in com_apply_people:
                    save.append(like.index(apply_num))
                save.sort()

                # 거절당한 지원자를 넣어준다.
                for rej in range(len(com_apply_people)-1, limit-1, -1):
                    reject.append(like[save.pop(rej)])

                select = []
                for sa in save:
                    select.append(like[sa])

                company_select[compaines[i][0]] = select

    while reject:
        put(reject)
        reject = []
        match(compaines, cnt_com, cnt_apply)

    for company in company_select:
        base = company + "_"
        for person in company_select[company]:
            base += person

        answer.append(base)

    return answer


print(solution(["A fabdec 2", "B cebdfa 2", "C ecfadb 2"], ["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"]))