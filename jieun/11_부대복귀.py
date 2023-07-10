import heapq


def solution(n, roads, sources, destination):
    edges = [[] for _ in range(n + 1)]
    for a, b in roads:
        edges[a].append(b)
        edges[b].append(a)

    INF = int(1e9)
    dist = [INF for _ in range(n + 1)]

    que = [(0, destination)]
    dist[destination] = 0

    while que:
        cur_dist, cur = heapq.heappop(que)
        if dist[cur] < cur_dist:
            continue

        for next in edges[cur]:
            next_dist = cur_dist + 1
            if dist[next] > next_dist:
                dist[next] = next_dist
                heapq.heappush(que, (next_dist, next))

    answer = [dist[s] if dist[s] < INF else -1 for s in sources]
    return answer
