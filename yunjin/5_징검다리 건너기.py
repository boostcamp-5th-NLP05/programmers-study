# 통과 풀이 (https://velog.io/@vkdldjvkdnj/programmers64062)
import heapq
from math import inf

n = len(stones)
def solution(stones, k):

    # 최대 힙 방식으로 각 구간의 최댓값을 구할 것이다.
    queue = []
    answer = inf

    # 먼저 0부터 k - 2 까지 최대 힙에 인덱스와 함께 넣자.
    for i in range(k - 1):
        heapq.heappush(queue, [-stones[i], i])

    # k - 1부턴 하나씩 최대 힙에 넣자.
    # 최대 힙의 맨 앞의 인덱스가 i - k + 1보다 작다면 구간을 벗어난 원소
    # 구간을 벗어난 원소를 전부 pop
    for i in range(k - 1, n):
        heapq.heappush(queue, [-stones[i], i])
        while queue[0][1] < i - k + 1:
            heapq.heappop(queue)
        answer = min(answer, -queue[0][0]) # 답은 각 구간의 최댓값들의 최솟값

    return answer




# 실패 풀이
def solution(stones, k):
    answer = int(1e9)
    r = []

    if k >= len(stones):
        return max(stones)

    for i in range(0, len(stones) - k + 1):
        ma = max(stones[i:i + k])
        mi = min(stones[i:i + k])
        x = ma - mi

        # 갭이 k 보다 작으면, 건너다가 더 이상 못건너게 되는 상황이 발생함.
        if x <= k:
            # 그 구간의 최댓값을 구하면 그것은 최소 건널 수 있다는 것이 됨.
            # 그 것들 중의 최소값이 전체 건널 수 있는 것 중 최소 친구 수가 됨.
            answer = min(answer, ma)

    return answer