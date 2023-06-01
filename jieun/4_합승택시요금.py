import heapq


def solution(n, s, a, b, fares):
    answer = 0

    edges = [[] for _ in range(n+1)]
    for x,y, cost in fares:
        edges[x].append((y, cost))
        edges[y].append((x, cost))

    INF = int(2e9)

    dist = [[INF for _ in range(n+1)] for _ in range(n+1)]
    dist[s][s] = 0  # [A위치][B위치]
    q = [(0, s, s)]

    while q:
        cost, a_cur, b_cur = heapq.heappop(q)
        if dist[a_cur][b_cur] < cost:
            continue
        if a_cur == a and b_cur == b:
            break

        if a_cur == a:
            for nb, nbc in edges[b_cur]:
                next_cost = cost + nbc
                if dist[a_cur][nb] > next_cost:
                    dist[a_cur][nb] = next_cost
                    heapq.heappush(q, (next_cost, a_cur, nb))
        elif b_cur == b:
            for na, nac in edges[a_cur]:
                next_cost = cost + nac
                if dist[na][b_cur] > next_cost:
                    dist[na][b_cur] = next_cost
                    heapq.heappush(q, (next_cost, na, b_cur))
        else:
            for na, nac in edges[a_cur]:
                for nb, nbc in edges[b_cur]:
                    if a_cur == b_cur and na == nb:  # 합승 중
                        next_cost = cost + nac  # nac == nbc
                        if dist[na][nb] > next_cost:
                            dist[na][nb] = next_cost
                            heapq.heappush(q, (next_cost, na, nb))
                    else:  # 따로 다른 길 가는 중
                        next_cost = cost + nac + nbc
                        if dist[na][nb] > next_cost:
                            dist[na][nb] = next_cost
                            heapq.heappush(q, (next_cost, na, nb))

    answer = dist[a][b]
    return answer
