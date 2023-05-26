def solution(sequence):
    max_val = -999999999

    n = len(sequence)
    if n == 1:
        return abs(sequence[0])

    # [1, -1, 1, ...]과 [-1, 1, -1, ...]를 각각 곱해서 먼저 펄스 수열 2개 만들어주기
    pulse_sequence_1 = [
        val if idx % 2 != 0 else -val for idx, val in enumerate(sequence)
    ]
    pulse_sequence_2 = [
        val if idx % 2 == 0 else -val for idx, val in enumerate(sequence)
    ]

    # 최대합 부분배열 DP로 구하기
    max_val = pulse_sequence_1[0]
    cur_sum = 0 # 현재 idx까지의 최대합 부분배열의 합
    for idx in range(n):
        # 새로운 값이 더 크면 그 값을 새로운 최대합 부분배열의 시작으로 교체
        cur_sum = max(pulse_sequence_1[idx], cur_sum + pulse_sequence_1[idx])
        max_val = max(max_val, cur_sum)

    cur_sum = 0
    for idx in range(n):
        cur_sum = max(pulse_sequence_2[idx], cur_sum + pulse_sequence_2[idx])
        max_val = max(max_val, cur_sum)

    return max_val
