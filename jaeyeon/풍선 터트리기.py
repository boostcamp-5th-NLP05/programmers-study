def solution(a):
    n = len(a)
    # 왼쪽값 중 최소값 저장
    left_min = [2e9 for _ in range(n)]
    left_min[0] = a[0]
    for idx in range(1, n):
        left_min[idx] = min(a[idx], left_min[idx - 1])

    # 오른쪽값 중 최소값 저장
    right_min = [2e9 for _ in range(n)]
    right_min[n - 1] = a[n - 1]
    for idx in range(n - 2, -1, -1):
        right_min[idx] = min(a[idx], right_min[idx + 1])

    no_cnt = 0
    for idx in range(n):
        # 양쪽 최소값보다 크면 살아남을 수 없음
        if a[idx] > left_min[idx] and a[idx] > right_min[idx]:
            no_cnt += 1

    return n - no_cnt
