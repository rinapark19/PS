from collections import deque

def solution(tickets):
    answer = []
    
    queue = deque()
    
    # 시작 지점이 인천이고, 알파벳 순으로 빠른 거 찾기
    begin = "Z"
    for i in range(len(tickets)):
        index = 0
        if tickets[i][0] == "ICN":
            if tickets[i][1] < begin:
                begin = tickets[i][1]
                index = i
                
    queue.append(tickets[index])
    answer.append("ICN")
    answer.append(tickets[index][1])
    tickets.pop(index)
    
    # BFS 수행
    while queue:
        ticket = queue.popleft()
        
        if len(tickets) == 0:
            return answer
        else:
            for t in tickets:
                if ticket[1] == t[0]:
                    queue.append(t)
                    answer.append(t[1])
                    tickets.remove(t)
                    print(f"BFS 수행 중: {answer}")

if __name__ == "__main__":
    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
    print(solution(tickets))