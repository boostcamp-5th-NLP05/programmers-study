def solution(n, roads, sources, destination):
    import heapq
    
    answer = []
    inf = 1e9
    start = destination
    graph = [[] for i in range(n+1)]
    distance = [inf for i in range(n+1)]
    
    for i,j in roads:
        graph[i].append((j,1))
        graph[j].append((i,1))
        
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    
    for i in sources:
        if distance[i] != inf:
            answer.append(distance[i])
        else:
            answer.append(-1)
            
    return answer