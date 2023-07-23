import heapq

def solution(n, cores):

    if n <= len(cores):
        return n

    core_list = []
    temp_core_list = []
    for i in range(len(cores)): #코어 번호 반영 및 작은 코어부터 처리하기 위함
        temp_core_list.append([cores[i], i+1]) # 코어 넣기
    temp_core_list.sort()

    for t in range(len(temp_core_list)):
        a, b = temp_core_list[t]
        heapq.heappush(core_list, (0, a, b)) # 코어 넣기
    temp_n = 1
    while True:
        # temp_n 증가 n이 되면 멈춤
        temp_core, core, core_num = heapq.heappop(core_list)
        if temp_n == n:
            return core_num
    
        temp_n += 1
        temp_core += core
        heapq.heappush(core_list, (temp_core, core, core_num))
        
        
        
print(solution(6,[1,2,3]))
