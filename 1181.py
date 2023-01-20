import sys

n = int(sys.stdin.readline())
li = []

for i in range(n):
    li.append(sys.stdin.readline().strip())

set1 = set(li)
li = list(set1)
li.sort()
li.sort(key = len)

for i in li:
    print(i)

# input이 엄청 느려서 stdin 써야 함
# 정렬 알고리즘 써서 하려고 했는데 시간 초과
# 내장된 sort에 key를 지정할 수 있다는 것을 몰랐음