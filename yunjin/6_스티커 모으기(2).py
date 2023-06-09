def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    # 0 인덱스 부터 ~ n - 1 인덱스까지
    dp = [0] * len(sticker)
    dp[0] = sticker[0]
    dp[1] = max(dp[0], sticker[1])

    for i in range(2, len(sticker)):
        i %= len(sticker)
        dp[i] = max(dp[i - 2] + sticker[i], dp[i - 1])  # i-1 를 다시 붙이고 i 번째를 뗄껀지 vs 현상 유지


    # -1 인덱스 부터 ~ n - 2 인덱스까지
    dp2 = [0] * len(sticker)
    dp2[0] = sticker[-1]
    dp2[1] = max(dp2[0], sticker[0])

    for i in range(2, len(sticker)):
        i %= len(sticker)

        # dp 순서는 유지하되 sticker[i - 1] 로 바꿔줘서 -1 번째부터 n-2 까지 비교함.
        dp2[i] = max(dp2[i - 2] + sticker[i - 1], dp2[i - 1])


    # 0 번째 인덱스 부터 고려 , -1 번째 인덱스 부터 고려를 통합해서 최댓값을 구해주면 된다.
    x = max(dp[:-1])
    y = max(dp2[:-1])
    answer = max(x, y)

    return answer