from collections import deque

def solution(stones, k):

    temp = deque(stones[0:k])
    temp_max = max(temp)

    if k == 1:
        return min(stones)
    max_list = []
    for i in range(k,len(stones)):

        temp_pop = temp.popleft()
        temp.append(stones[i])
        # k만큼 돌을 묶어서 그중에 가장 큰값 append
        # 슬라이싱을 그때마다 해주는 방법 -> deque에 추가, 삭제방법으로 변경
        # if temp_pop == temp_max: # 조건으로 연산량 줄임
        #     temp_max = max(temp)
        
        max_list.append(max(temp))

    return min(max_list)

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))