def solution(n, s, a, b, fares):
    INF = int(1e9)
    answer = INF

    # 플로이드워셜 적용을 위한 초기화
    map_ = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    for idx in range(n + 1):
        map_[idx][idx] = 0

    for src, dst, fare in fares:
        map_[src][dst] = fare
        map_[dst][src] = fare

    # 플로이드워셜 수행
    for k in range(1, n + 1):
        for src in range(1, n + 1):
            for dst in range(1, n + 1):
                map_[src][dst] = min(map_[src][dst], map_[src][k] + map_[k][dst])

    # 갈라지는 지점 완전탐색으로 찾기
    for idx in range(1, n + 1):
        val = map_[s][idx] + map_[idx][a] + map_[idx][b]
        answer = min(answer, val)

    return answer
