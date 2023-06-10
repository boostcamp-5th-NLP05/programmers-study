def get_max(sticker):
    n = len(sticker)

    # dp 초기값 설정
    dp = [0] * n
    dp[0] = sticker[0]
    dp[1] = sticker[1]

    # 마지막 수는 버리고 n - 1까지만 구하기
    for idx in range(2, n - 1):
        dp[idx] = max(dp[idx - 1], dp[idx - 2] + sticker[idx])

    return max(dp)


def solution(sticker):
    # 특이 케이스들 미리 구하기
    if len(sticker) == 1:
        return sticker[0]

    if len(sticker) == 2:
        return max(sticker)

    # 스티커 돌리기
    turn1 = sticker[1:] + [sticker[0]]
    turn2 = sticker[2:] + sticker[:2]

    answer = max(get_max(sticker), get_max(turn1), get_max(turn2))

    return answer
