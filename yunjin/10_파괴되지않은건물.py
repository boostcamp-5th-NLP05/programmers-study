def skil_effect(board, skill_one, map_):
    t, r1, c1, r2, c2, degree = skill_one

    r2 += 1
    c2 += 1

    if t == 1:  # 감소 스킬
        for r in range(r1, r2):
            for c in range(c1, c2):
                map_[r][c].append(-degree)
    else:  # 회복 스킬
        for r in range(r1, r2):
            for c in range(c1, c2):
                map_[r][c].append(degree)

    return board, map_


def solution(board, skill):
    answer = 0

    map_ = [[[board[j][i]] for i in range(len(board[0]))] for j in range(len(board))]

    # 반복
    for i in range(len(skill)):
        board, map_ = skil_effect(board, skill[i], map_)

    # 계산
    for i in range(len(board)):
        for j in range(len(board[0])):
            if sum(map_[i][j]) >= 1:
                answer += 1

    return answer