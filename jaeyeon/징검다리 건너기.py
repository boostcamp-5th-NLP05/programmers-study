# 효율성에서 걸린 풀이
def solution1(stones, k):
    if k == 1:
        return min(stones)

    min_val = 2000001
    for idx in range(0, len(stones) - k):
        # 구간별 최대값들 중 최소값 구하기
        min_val = min(min_val, max(stones[idx : idx + k]))

    return min_val


# 참고한 풀이
def can_go(n, stones, k):
    zero_cnt = 0
    for stone in stones:
        if stone < n:
            zero_cnt += 1
            if zero_cnt == k:
                return False
        else:
            zero_cnt = 0
    return True


def solution2(stones, k):
    answer = 1
    left, right = 1, max(stones)

    while left <= right:
        mid = (left + right) // 2
        if can_go(mid, stones, k):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer
