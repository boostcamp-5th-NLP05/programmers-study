def solution(stones, k):
    if k == 1:
        return min(stones)
    max_list = []
    for i in range(k,len(stones)):
        max_list.append(max(stones[i-k:i]))
        # k만큼 돌을 묶어서 그중에 가장 큰값 append

    return min(max_list)

solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)