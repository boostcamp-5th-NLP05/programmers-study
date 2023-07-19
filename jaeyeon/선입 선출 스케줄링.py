def solution(n, cores):
    if n < len(cores):
        return n

    # 전체 소요 시간 이진 탐색으로 찾기
    left, right = 1, max(cores) * n
    while left < right:
        mid = (left + right) // 2
        work_count = sum([mid // core for core in cores])

        if work_count < n:
            left = mid + 1
        else:
            right = mid
    # left : 4

    # 매 시간마다 작업할 수 있는 코어 개수 찾기
    work_hour = left
    times = [0 for _ in range(work_hour)]
    for core in cores:
        for idx in range(0, work_hour, core):
            times[idx] += 1
    # times : [3, 1, 2, 2]

    # 이진 탐색으로 times에서 작업이 끝나는 시간 확인하기
    left, right = 1, work_hour
    while left < right:
        mid = (left + right) // 2

        work_sum = sum(times[:mid])
        if work_sum < n:
            left = mid + 1
        else:
            right = mid
    # left : 3
    last_time = left

    target = n - sum(times[: last_time - 1])  # 마지막 시간에 마지막으로 일하는 코어의 순서
    cur_sum = 0

    # 마지막 시간에 target번째로 일하는 코어 찾기
    for idx, core in enumerate(cores):
        if (last_time - 1) % core == 0:
            # 일할 수 있는 코어가 있으면 cur_sum 증가
            cur_sum += 1
            if cur_sum == target:
                return idx + 1


print(solution(6, [1, 2, 3]))
