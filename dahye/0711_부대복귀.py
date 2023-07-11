def solution(n, roads, sources, destination):
    answer = []
    INF = int(1e9)

    # 2차원 리스트 (그래프 표현) 만들고, 무한대로 초기화
    graph = [[INF] * (n + 1) for _ in range(n + 1)]


    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0

    # 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
    for road in roads:
        # A -> B로 가는 비용을 C라고 설정
        a, b = road
        graph[a][b] = 1
        graph[b][a] = 1 # 서로 이어졌으므로

    # 점화식에 따라 플로이드 워셜 알고리즘을 수행
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    # destination에서 s까지 방문의 최소시간
    for s in sources:
        ans = graph[destination][s]
        if ans >= INF:
            answer.append(-1)
        else:
            answer.append(ans)
    
    return answer

n = 5
roads = [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]]
sources = [1,3,5]
destination = 5
print(solution(n, roads, sources, destination))

