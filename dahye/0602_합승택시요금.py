import heapq

def dijkstra(n, start, end, graph): # 다익스트라 알고리즘
    q = []
    INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정
    distance = [INF] * (n+1)
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    
    return distance[end]


def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    INF = int(1e9)

    for i in range(len(fares)):
        x,y,z = fares[i]
        graph[x].append((y,z))
        graph[y].append((x,z)) # 양 방향 이동가능

    answer = INF
    for random in range(1,n+1):
        answer = min(answer,dijkstra(n, s, random, graph) + dijkstra(n, random, a, graph) + dijkstra(n, random, b, graph))
    return answer


print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))