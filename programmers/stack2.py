def solution(progresses, speeds):
    answer = []
    stack = []
    
    for i in range(len(progresses)):
        date = (100 - progresses[i]) / speeds[i]
        date_int = (100 - progresses[i]) // speeds[i]
        
        if date > date_int:
            date = date_int + 2
        
        stack.append(int(date))
    
    i = 0
    j = i + 1
    while j < len(stack):
        num = 1
        # 첫번째 거가 다음 것보다 큰 경우(그럼 얘보다 작은 숫자를 다 찾아야 함)
        if stack[i] >= stack[j]:
            # 계속 작은 동안
            while stack[i] >= stack[j]:
                j += 1
                num += 1
                if j >= len(stack):
                    break
            answer.append(num)
            # 기준 새로 정하기
            i = j
            j = i + 1
        
        # 첫번째 거가 다음 것보다 작은 경우
        else:
            answer.append(num)
            # 기준 새로 정하기
            i = j
            j = i + 1
    
    if j == len(stack):
        answer.append(1)
    
    return answer

if __name__ == "__main__":
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]

    print(solution(progresses, speeds))