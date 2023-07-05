def solution(board, skill):
    answer = 0 # 누적 정보 저장
    temp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for s in range(len(skill)):
        if skill[s][0] == 1: # 공격일 때
            temp[skill[s][1]][skill[s][2]] -= skill[s][5]
            # 공격 끝나는 지점
            temp[skill[s][1]][skill[s][4]+1] += skill[s][5]
            temp[skill[s][3]+1][skill[s][2]] += skill[s][5]
            # 복구
            temp[skill[s][3]+1][skill[s][4]+1] -= skill[s][5]
        else:
            temp[skill[s][1]][skill[s][2]] += skill[s][5]
            #방어 끝나는 지점
            temp[skill[s][1]][skill[s][4]+1] -= skill[s][5]
            temp[skill[s][3]+1][skill[s][2]] -= skill[s][5]
            # 복구
            temp[skill[s][3]+1][skill[s][4]+1] += skill[s][5]
    # 누적합
    for i in range(len(board)): 
        for j in range(len(board[0])-1):
            temp[i][j + 1] += temp[i][j]
    for j in range(len(board[0])): 
        for i in range(len(board)-1):
            temp[i + 1][j] += temp[i][j]
    
    # 합치기
    for x in range(len(board)):
        for y in range(len(board[0])):
            board[x][y] += temp[x][y]
            if board[x][y] > 0: # 0이 넘으면 파괴되지 않음
                answer += 1
    
    return answer

print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))