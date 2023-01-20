N = int(input())

lst = list(map(int, input().split()))

# 걸리는 시간을 정렬
lst.sort()

result = 0
time = 0
# 시간을 결과와 시간변수에 넣어준다.
for person in lst:
    time += person
    result += time

print(result)
