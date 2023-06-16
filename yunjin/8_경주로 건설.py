from collections import deque


def solution(board):
    answer = 0
    N = len(board)
    d = deque()

    visited = [[False for i in range(N)] for j in range(N)]

    visited[0][0] = True

    # 남 북 동 서
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    result = []

    d.append([0, 1, 1, 0, 2, 100])
    d.append([1, 0, 1, 0, 0, 100])
    visited[0][1] = True
    visited[1][0] = True

    map_ = [[] for i in range(N) for j in range(N)]

    print(map_)

    while d:

        r, c, f, t, direc, money = d.popleft()
        print(r, c, f, t, direc, money)

        if r == N - 1 and c == N - 1:
            result.append([f, t])

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if board[nr][nc] == 1:
                continue

            if not visited[nr][nc]:
                if direc == i:
                    new_money = 100 * (f + 1) + 500 * t
                    d.append([nr, nc, f + 1, t, i, new_money])
                else:
                    new_money = 100 * (f + 1) + 500 * t
                    d.append([nr, nc, f + 1, t + 1, i, new_money])

                visited[nr][nc] = True

    print(result[0])
    x = result[0]
    answer = 100 * x[0] + 500 * x[1]

    return answer