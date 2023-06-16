import heapq
def solution(n, times):
    answer=0
    people = 0
    time = []
    for i in times:
        time.append([i,i])
    while people<n:
        finish, simsadae = heapq.heappop(time)
        
        heapq.heappush(time,[finish+simsadae,simsadae])
        people += 1
    answer=max(answer, finish)    
    return answer

print(solution(6,[7, 10]))