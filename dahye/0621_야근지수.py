import heapq

def solution(n, works):
    
    if sum(works) < n:
        return 0
    temp = []
    for w in works:
        heapq.heappush(temp, (-w, w)) # 역순으로 넣기
    while n != 0:
        max_work = heapq.heappop(temp)[1]
        max_work -= 1
        n -= 1
        heapq.heappush(temp, (-max_work, max_work))

    for i in range(len(temp)):
        answer += (temp[i][1])**2

    return answer


print(solution(3,[1,1]))