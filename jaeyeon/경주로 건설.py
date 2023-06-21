from collections import deque


def solution(board):
    min_val = int(1e9)
    n = len(board)

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    # 각 지점별로 지나갈 때의 비용 저장할 배열
    visited = [[int(1e9) for _ in range(n)] for _ in range(n)]
    visited[0][0] = 0

    q = deque()
    q.append([0, 0, 0, 0])

    while q:
        cur_r, cur_c, cur_dir, cost = q.pop()
        for dir_ in range(4):
            next_r = cur_r + dr[dir_]
            next_c = cur_c + dc[dir_]

            if next_r in [-1, n] or next_c in [-1, n]:
                continue

            if board[next_r][next_c] == 1:
                continue

            # 처음엔 직선만 생기므로
            if cost == 0:
                cur_cost = 100
            else:
                cur_cost = 100 if dir_ == cur_dir else 600

            # 다음 좌표가 끝이면 최소 비용과 비교
            if next_r == n - 1 and next_c == n - 1:
                min_val = min(min_val, cur_cost + cost)

            # 약간의 여유를 둬서 돌아가더라도 최소 비용으로 가는 케이스 잡기
            if visited[next_r][next_c] + 400 >= cost + cur_cost:
                visited[next_r][next_c] = cost + cur_cost
                q.append([next_r, next_c, dir_, cost + cur_cost])

    return min_val
