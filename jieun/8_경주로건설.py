import heapq


def solution(board):
    answer = 0
    N = len(board)

    # 위, 오른, 아래, 왼
    steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    START = (0, 0)
    STRAIGHT_COST = 100  # 직선 도로 비용
    CORNER_COST = 500  # 코너 도로 비용
    INF = int(1e9)

    cost = [[INF for _ in range(N)] for _ in range(N)]
    cost[0][0] = 0

    # 현재 비용, (현재 위치), 전 방향
    q = [(-CORNER_COST, START, 1), (-CORNER_COST, START, 2)]
    # 첫 번째 코너를 도는 경우는 가짜이므로 값을 미리 빼준다.

    while q:
        cur_cost, (cur_r, cur_c), cur_d = heapq.heappop(q)

        opposite_dir = (cur_d + 2) % 4
        for nd in range(4):
            if nd in [cur_d, opposite_dir]:  # 코너를 돌지 않는 방향은 제외
                continue
            nr = cur_r
            nc = cur_c
            ncost = cur_cost + CORNER_COST
            for _ in range(N):  # 벽이 나올 때까지 직선으로 탐색
                nr += steps[nd][0]
                nc += steps[nd][1]
                ncost += STRAIGHT_COST
                if nr in [-1, N] or nc in [-1, N]:
                    break
                if board[nr][nc] == 1:
                    break
                if ncost < cost[nr][nc]:
                    cost[nr][nc] = ncost
                    heapq.heappush(q, (ncost, (nr, nc), nd))

    answer = cost[N - 1][N - 1]
    return answer
