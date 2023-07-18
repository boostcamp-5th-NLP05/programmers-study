import heapq
def solution(n, cores):
    answer = 0

    h = []
    for i in range(len(cores)):
        heapq.heappush(h, [cores[i], i])

    if n <= len(cores):
        return n

    n -= len(cores)

    while True:
        value, idx = h[0]

        h.sort(key=lambda x: (x[0], x[1]))
        for i in range(len(h)):
            if h[i][0] == value:
                n -= 1
                h[i][0] = cores[h[i][1]]

                if n == 0:
                    return h[i][1] + 1
            else:
                h[i][0] -= value

    return answer