def solution(board, skill):
    N = len(board)
    M = len(board[0])

    change = [[0 for _ in range(M)] for _ in range(N)]

    # change[r][c]: 직사각형 (0,0) ~ (r,c) 에 더할 값
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree *= -1
        change[r2][c2] += degree
        if r1 > 0 and c1 > 0:
            change[r1 - 1][c1 - 1] += degree
        if r1 > 0:
            change[r1 - 1][c2] -= degree
        if c1 > 0:
            change[r2][c1 - 1] -= degree

    # change[r][c]: 칸 (r,c) 내구도 변경 값
    for r in range(N - 1, -1, -1):
        for c in range(M - 1, -1, -1):
            if r + 1 < N:
                change[r][c] += change[r + 1][c]
            if c + 1 < M:
                change[r][c] += change[r][c + 1]
            if r + 1 < N and c + 1 < M:
                change[r][c] -= change[r + 1][c + 1]

    answer = 0

    # 파괴되지 않은 빌딩 개수 세기
    for r in range(N):
        for c in range(M):
            if change[r][c] + board[r][c] > 0:
                answer += 1

    return answer
