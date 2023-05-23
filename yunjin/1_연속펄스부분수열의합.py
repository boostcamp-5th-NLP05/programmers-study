def first_check(i, sequence, dp, fulse):
    x = sequence[i - 1] - sequence[i]
    y = -sequence[i - 1] + sequence[i]

    if x <= sequence[i - 1] and y <= sequence[i - 1]:
        dp[i - 1][0] = sequence[i - 1]
        dp[i - 1][1] = 1
        fulse = 1
        return

    if x > 0 and y > 0:

        if x > y:
            dp[i - 1][0] = sequence[i - 1]
            dp[i - 1][1] = 1
            dp[i][0] = x
            dp[i][1] = 2
            fulse = 1  # 양수로 전환
        else:
            dp[i - 1][0] = sequence[i - 1] * (-1)
            dp[i - 1][1] = 1
            dp[i][0] = y
            dp[i][1] = 2
            fulse = -1  # 음수로 전환
    elif x > 0:
        dp[i - 1][0] = sequence[i - 1]
        dp[i - 1][1] = 1
        dp[i][0] = x
        dp[i][1] = 2
        fulse = 1  # 양수로 전환
    elif y > 0:
        dp[i - 1][0] = sequence[i - 1] * (-1)
        dp[i - 1][1] = 1
        dp[i][0] = y
        dp[i][1] = 2
        fulse = -1  # 음수로 전환



# 500,000 개 여서 이진탐색 or dp 로 생각했고, 수열 문제여서 느낌 상 dp 로 품.
def solution(sequence):
    result = []

    answer = 0

    dp = [[0, 0] for i in range(500001)]

    fulse = 1  # 펄스 [1, -1]

    for i in range(1, len(sequence)):

        if dp[i - 1][0] == 0: # 시작점의 부분 진행 수열이 0 이라면 pulse 를 1로 시작할지 -1로 시작할지 정해준다.
            first_check(i, sequence, dp, fulse)
            continue

        # 펄스 곱을 계속해서 진행했을 때 값이 작아지는 지점을 발견하면 펄스 부분수열을 새롭게 시작할지, 그래도 진행할 지 정해준다.
        if dp[i - 1][0] + sequence[i] * fulse < 0:
            if sequence[i] > dp[i - 1][0] + sequence[i] * fulse: # 펄스 부분수열을 새롭게 시작할지, 그래도 진행할 지 이곳에서 정해준다.
                first_check(i, sequence, dp, fulse)
            else:
                result.append(dp[i - 1][0])
                continue

        elif dp[i - 1][0] + sequence[i] * fulse == 0:
            continue

        else: # 펄스 부분수열을 그대로 진행 처리.
            dp[i][0] = dp[i - 1][0] + sequence[i] * fulse
            dp[i][1] = dp[i][1] + 1
            fulse *= -1  # 음수로 전환

        result.append(dp[i - 1][0])

    # print(result)
    answer = max(result)

    return answer
