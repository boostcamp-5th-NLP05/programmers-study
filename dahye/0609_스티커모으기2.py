from collections import deque

def solution(sticker): #bfs
    answer = []
    queue = deque()
    for i in range(min(len(sticker), 3)):
        queue.append((sticker[i], i, i))
    while queue:
        i, idx, first_idx = queue.popleft() # 가장 앞 스티커와 맨 뒤 스티커는 함께 뗄 수 없으므로
        if not(idx == (len(sticker)-1) and first_idx == 0):
            answer.append(i)
        for di in ([2,3]): #다음 step 2칸 옆 or 3칸 옆
            ni = idx + di
            if ni < len(sticker) :
                queue.append((i + sticker[ni], ni, first_idx))

             

    return max(answer)

print(solution([5, 1, 16, 17, 16]))