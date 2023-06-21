import heapq


def solution(n, works):
    answer = 0

    if n >= sum(works):
        return 0

    heap = []

    # 힙에 역순으로 넣기
    for work in works:
        heapq.heappush(heap, (-work, work))

    while True:

        # 큰 값 부터 빼기
        h = heapq.heappop(heap)[1]

        n -= 1
        h -= 1
        heapq.heappush(heap, (-h, h))

        if n == 0:
            break

        if len(heap) <= 1:
            break

    # 결과
    for i in range(len(heap)):
        answer += heap[i][1] * heap[i][1]

    return answer