# 입실 시간 리스트가 필요, 같은 시간이라면 따른 객실을 주어야함
# 방 리스트가 필요하다. 부족하면 append 나가면 -2로 표시하고 청소가 완료되면 -1로 표시한다.
# 들어가 있는 사람은 idx로 저장
from collections import deque


def solution(book_time):
    answer = 0

    rooms = []

    # 예약시간이 빠른 순으로 정렬
    book_time.sort()

    # 초기값 설정
    enter, out = book_time.pop(0)

    if len(rooms) == 0:
        rooms.append(out)

    while book_time:
        enter, out = book_time.pop(0)

        add = True
        for i in range(len(rooms)):
            room = rooms[i]
            if enter < room:
                continue
            elif enter[:2] == room[:2] and int(enter[3:]) - int(room[3:]) < 10:
                continue
            elif int(enter[:2]) - int(enter[:2]) == 1 and int(room[3:]) - int(enter[3:]) > 50:
                continue
            else:
                add = False
                rooms[i] = out
                break

        if add:
            rooms.append(out)

    return len(rooms)

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))