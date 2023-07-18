import heapq

def solution(n, cores):

    core_list = []
    cores.sort()

    for i in range(len(cores)):
        heapq.heappush(core_list, (0, cores[i])) # 코어 넣기
    temp_n = 0
    while True:
        # temp_n 증가 n이 되면 멈춤
        temp_core, core = heapq.heappop(core_list)
    
        temp_n += 1
        temp_core += core
        heapq.heappush(core_list, (temp_core, core))
        print(temp_core, core)
        if temp_n == n:
            return core
        
print(solution(6,[1,2,3]))
