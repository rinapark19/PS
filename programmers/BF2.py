p1 = [1, 2, 3, 4, 5] # len: 5
p2 = [2, 1, 2, 3, 2, 4, 2, 5] # len: 8
p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # len: 10

def solution(answers):
    answer = []
    
    # 각 사람이 맞힌 문제 개수
    c1 = 0
    c2 = 0
    c3 = 0
    
    # 각 사람의 찍는 규칙 리스트 이터레이터
    i1 = 0
    i2 = 0
    i3 = 0
    
    for a in answers:
        # 이터레이터가 리스트 넘어갔는지 확인
        if i1 == 5:
            i1 = 0
        
        if i2 == 8:
            i2 = 0
        
        if i3 == 10:
            i3 = 0
        
        # 문제 맞았는지 확인해서 점수 매기기
        if p1[i1] == a:
            c1 += 1
        
        if p2[i2] == a:
            c2 += 1
        
        if p3[i3] == a:
            c3 += 1
        
        # 각 이터레이터 늘려 주기
        i1 += 1
        i2 += 1
        i3 += 1
    
    # 조건에 따라 정답 반환
    if c1 > c2 and c1 > c3:
        answer.append(1)
    elif c2 > c1 and c2 > c3:
        answer.append(2)
    elif c3 > c1 and c3 > c2:
        answer.append(3)
    elif c1 == c2 and c1 > c3:
        answer.append(1)
        answer.append(2)
    elif c2 == c3 and c2 > c1:
        answer.append(2)
        answer.append(3)
    elif c3 == c1 and c1 > c2:
        answer.append(1)
        answer.append(3)
    elif c1 == c2 and c2 == c3:
        answer.append(1)
        answer.append(2)
        answer.append(3)
        
    return answer

if __name__ == "__main__":
    print(solution([1, 2, 3, 4, 5]))