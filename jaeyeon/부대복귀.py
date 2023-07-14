from collections import deque


def solution(n, roads, sources, destination):
    # 인접 리스트로 그래프 초기화
    can_go = [[] for _ in range(n + 1)]
    for src, dst in roads:
        can_go[src].append(dst)
        can_go[dst].append(src)

    # 거리 배열 초기화
    dist = [-1 for _ in range(n + 1)]
    dist[destination] = 0

    # 다익스트라 실행
    q = deque([destination])
    while q:
        cur_pos = q.popleft()
        next_dist = dist[cur_pos] + 1
        for dst in can_go[cur_pos]:
            if dist[dst] == -1:
                dist[dst] = next_dist
                q.append(dst)

    return [dist[s] for s in sources]
