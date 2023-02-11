# 한 번에 한명의 유저가 신고
# k 번 이상 신고를 당하면 정지
# 신고 처리 결과 메일을 몇번 보내면 되나

def solution(id_list, report, k):
    answer = {}
    repo_cnt = {}

    # '유저이름': {신고한 유저목록}
    for lst in id_list:
        answer[lst] = set()
        repo_cnt[lst] = 0

    for repo in report:
        a, b = repo.split(" ")
        answer[a].add(b)

    # 유저가 신고한 사람의 신고횟수를 카운트
    for name in answer:
        for repo in answer[name]:
            repo_cnt[repo] += 1

    success = []
    # 일정 횟수를 넘으면 신고 성공에 넣어준다.
    for name in repo_cnt:
        if repo_cnt[name] >= k:
            success.append(name)

    result = []
    # 유저가 신고한 사람이 성공했으면 카운트 해주고 반환한다.
    for name in answer:
        cnt = 0
        for repo in answer[name]:
            if repo in success:
                cnt += 1

        result.append(cnt)

    return result