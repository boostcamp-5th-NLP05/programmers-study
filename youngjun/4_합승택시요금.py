def solution2(n, s, a, b, fares):
    #플로이드 워셜로 최소값 구하기
    inf = int(1e9)
    graph = [[inf for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(1,n+1):
        graph[i][i] = 0
    
    for i in fares:
        tmp1,tmp2,cost = i
        graph[tmp1][tmp2] = cost
        graph[tmp2][tmp1] = cost
        
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])
                
    answer = inf
    
    for k in range(1,n+1):
        answer = min(answer, graph[s][k] + graph[k][a] + graph[k][b])

    return answer

from heapq import heappush, heappop
def solution(n, s, a, b, fares):
    #다익스트라 3번으로 최소값 구하기
    graph = [[] for _ in range(n+1)]
    inf = int(1e9)
    
    for i in fares:
        graph[i[0]].append((i[1],i[2]))
        graph[i[1]].append((i[0],i[2]))
    
    cost1 = [inf for _ in range(n+1)]
    cost2 = [inf for _ in range(n+1)]
    cost3 = [inf for _ in range(n+1)]
    
    def da(start,cost_list):
        cost_list[start] = 0
        heap = [[0,start]]
        while heap:
            cost, loc = heappop(heap)
            
            if cost_list[loc] < cost:
                continue
            
            for i in graph[loc]:
                if cost + i[1] < cost_list[i[0]]:
                    cost_list[i[0]] = cost + i[1]
                    heappush(heap,(cost + i[1],i[0]))

    da(s,cost1)
    da(a,cost2)
    da(b,cost3)
    
    answer = inf
    
    for i in range(1,n+1): #모든 합승 구간 구해서 최소값 구하기
        answer = min(answer, cost1[i] + cost2[i] + cost3[i])
        
    return answer

