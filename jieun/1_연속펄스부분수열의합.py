def solution(sequence):
    answer = 0

    pulse = [sequence.copy(), sequence.copy()]
    # 0: -1 시작, 1: 1 시작

    # 펄스 수열 곱하기
    for i in range(len(sequence)):
        if i % 2 == 0:
            pulse[0][i] *= -1
        else:
            pulse[1][i] *= -1

    # 누적합 구하기
    for i in range(1, len(sequence)):
        for j in [0, 1]:
            pulse[j][i] += pulse[j][i-1]

    # 합이 가장 큰 부분 수열 구하기
    pulse_sum = [pulse[0][0], pulse[1][0]]
    pulse_min = [pulse[0][0], pulse[1][0]]
    for i in range(1, len(sequence)):
        for j in [0, 1]:
            # 부분 수열 [0번째 ~ i번째]와 [pulse_min~i번째] 중 최대 선택. pulse_min은 i번째 원소보다 앞에 있는 원소 중 최소값.
            sum_ = max(pulse[j][i], pulse[j][i] - pulse_min[j]) 
            pulse_min[j] = min(pulse_min[j], pulse[j][i])
            pulse_sum[j] = max(pulse_sum[j], sum_)

    answer = max(pulse_sum)

    return answer
