import heapq

def solution(n, roads, sources, destination):
    inf = 1e9
    answer = []
    graph = [[] for _ in range(n+1)]
    distance = [inf] * (n+1)

    for road in roads:
        a,b = road
        graph[a].append(b)
        graph[b].append(a)

    # 다익스트라 알고리즘 수행
    q = []
    heapq.heappush(q, (0,destination))
    distance[destination] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]: # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i] = cost
                heapq.heappush(q, (cost, i))

    # destination에서 s까지 방문의 최소시간
    for s in sources:
        if distance[s] != inf:
            answer.append(distance[s])
        else:
            answer.append(-1)
    
    return answer

n = 5
roads = [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]]
sources = [1,3,5]
destination = 5
print(solution(n, roads, sources, destination))
