import heapq
def solution(n, times):
    answer = 0
    times.sort()
    heap = []
    max_ = n * times[0] #최악의 경우
    
    for i in times:
        for j in range(1,max_//i+1):
            heapq.heappush(heap,i*j)

    for _ in range(n):
        answer = heapq.heappop(heap)

    return answer