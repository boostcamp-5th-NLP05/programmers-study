def solution(board, skill):
    answer = 0
    tmp = [[0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]
    
    for i in skill: #누적합 계산을 위한 값들 넣기
        type_, r1, c1, r2, c2, degree = i
        
        if type_ == 1:
            type_ = -1
        else:
            type_ = 1
        
        #첫 줄
        tmp[r1][c1] += type_ * degree
        tmp[r1][c2+1] -= type_ * degree
        
        #마지막 줄
        tmp[r2+1][c1] -= type_ * degree
        tmp[r2+1][c2+1] += type_ * degree

    #가로로 누적합
    for r in range(len(board)+1):
        cnt = 0
        for c in range(len(board[0])):
            cnt += tmp[r][c]
            tmp[r][c] = cnt
    
    #세로로 누적합
    for c in range(len(board[0])+1):
        cnt = 0
        for r in range(len(board)):
            cnt += tmp[r][c]
            tmp[r][c] = cnt
            
    for i in range(len(board)): #파괴되지 않은 건물 세기
        for j in range(len(board[0])):
            if board[i][j] > -1 * tmp[i][j]:
                answer += 1

    return answer