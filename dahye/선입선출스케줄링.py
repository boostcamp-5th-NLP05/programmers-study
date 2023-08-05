import heapq

def solution(n, cores):

    if n <= len(cores):
        return n

    core_list = []
    for i in range(len(cores)):
        heapq.heappush(core_list, (cores[i], cores[i], i+1)) # 코어 넣기
    temp_n = 0

    n -= len(cores)

    while True:
        # temp_n 증가 n이 되면 멈춤
        temp_core, core, core_num = heapq.heappop(core_list)
        
    
        temp_n += 1
        temp_core += core

        if temp_n == n:
            return core_num
        heapq.heappush(core_list, (temp_core, core, core_num))
        
        
        
print(solution(6,[1,2,3]))
