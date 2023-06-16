def isable(n, mid, times):
    total = [mid // time for time in times]
    return sum(total) >= n


def solution(n, times):
    left, right = 1, int(1e18)
    while left < right:
        mid = (left + right) // 2
        if isable(n, mid, times):
            right = mid
        else:
            left = mid + 1

    return left
