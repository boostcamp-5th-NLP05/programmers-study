def solution(a):
    INF = int(2e9)
    a_len = len(a)

    left_min = [INF for _ in range(a_len)]  # 왼쪽 끝부터 i 번째까지 최소값
    right_min = [INF for _ in range(a_len)]  # i 번째부터 오른쪽 끝까지 최소값

    left_min[0] = a[0]
    for i in range(1, a_len):
        left_min[i] = min(a[i], left_min[i - 1])

    right_min[a_len - 1] = a[a_len - 1]
    for i in range(a_len - 2, -1, -1):
        right_min[i] = min(a[i], right_min[i + 1])

    answer = 2  # 맨 끝은 항상 남을 수 있음

    for i in range(1, a_len - 1):
        if a[i] > left_min[i - 1] and a[i] > right_min[i + 1]:
            # 작은 값은 한 번만 터트릴 수 있으므로, i 번째 풍선이 왼쪽, 오른쪽 최소값보다 크면 남을 수 없음
            continue
        answer += 1

    return answer
