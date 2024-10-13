from itertools import permutations

MAX = 10000000
# 소수를 1로 표시
arr = [1] * (MAX+1)
arr[0] = 0
arr[1] = 0

for i in range(2, MAX+1):
    j = 2
    while i * j <= MAX:
        arr[i*j] = 0
        j += 1

def solution(numbers):
    answer = 0
    
    nums = list(numbers)
    per = []
    for i in range(1, len(numbers)+1):
        per += list(permutations(nums, i))
    new_nums = [int(("")).join((p)) for p in per]
    
    for num in new_nums:
        if arr[num] == 1:
            answer += 1
    
    return answer

if __name__ == "__main__":
    solution("117")