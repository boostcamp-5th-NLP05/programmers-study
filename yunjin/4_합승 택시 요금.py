import heapq  # 우선순위 큐 구현을 위함
import copy
from collections import deque


# def dijkstra(start):
#     q=[]
#     #시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
#     heapq.heappush(q, (0, start))
#     distance[start]=0

#     #q가 비어있지 않다면
#     while q:
#         #가장 최단 거리인 노드에 대한 정보 꺼내기
#         dist, now = heapq.heappop(q)
#         #현재 노드가 이미 처리됐다면 skip
#         if distance[now] < dist:
#             continue
#         #현재 노드와 연결된 다른 인접한 노드 확인
#         for i in graph[now]:
#             cost = dist + i[1]
#             #현재 노드를 거치면 이동 거리가 더 짧은 경우
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))


def solution(n, s, a, b, fares):
    answer = 0

    graph = [[] for i in range(n + 1)]

    print(graph)
    for start, end, dis in fares:
        graph[start].append([end, dis])
        graph[end].append([start, dis])

    visited = [False for i in range(n + 1)]

    print(graph)

    d = deque()
    d.append([s, 0, 0])

    check_point = []

    check_cnt = 0

    while d:

        s1, d1, cnt = d.popleft()

        if s1 == a:
            check_point.append((s1, d1))
            d1 = 0
            cnt += 1

        if s1 == b:
            check_point.append((s1, d1))
            d1 = 0
            cnt += 1

        if cnt == 2:
            break

        if not visited[s1]:
            visited[s1] = True

            for e2, d2 in graph[s1]:
                d.append([e2, d1 + d2, cnt])

    answer = check_point[0][1] + check_point[1][1]

    return answer