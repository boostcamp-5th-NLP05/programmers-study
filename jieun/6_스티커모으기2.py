def solution(sticker):
    answer = 0
    N = len(sticker)
    
    if N == 1:
        return sticker[0]

    # dp[i] = [i번째 포함, i번째 미포함]
    dp_left = [[0,0] for _ in range(N)] # 왼쪽 -> 오른쪽 순서 탐색
    dp_right = [[0,0] for _ in range(N)] # 오른쪽 -> 왼쪽 순서 탐색

    dp_left[0][0] = sticker[0]
    dp_right[N-1][0] = sticker[N-1]
    
    # 왼쪽에서부터 dp_left 채우기. 
    for i in range(1, N):
        dp_left[i][0] = dp_left[i-1][1] + sticker[i]
        dp_left[i][1] = max(dp_left[i-1])
    
    # 오른쪽에서부터 dp_right 채우기
    for i in range(N-2, -1, -1):
        dp_right[i][0] = dp_right[i+1][1] + sticker[i]
        dp_right[i][1] = max(dp_right[i+1])
    
    answer = max(dp_left[N-1][1], dp_right[0][1])

    return answer

sticker = [14, 6, 5, 11, 3, 9, 2, 10]
print(solution(sticker))