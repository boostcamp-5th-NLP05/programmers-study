import heapq


def dijkstra(graph, start):
    distances = [float('inf') for node in graph]
    distances[start] = 0

    queue = []

    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)
        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination]:
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])

    return distances


def solution(n, roads, sources, destination):
    graph = [[] for i in range(n + 1)]
    graph[0].append([0, 0])

    for road in roads:
        s, e = road
        graph[s].append([e, 1])
        graph[e].append([s, 1])

    x = dijkstra(graph, destination)

    result = []
    for s in sources:
        if x[s] == float('inf'):
            result.append(-1)
        else:
            result.append(x[s])
    return result
