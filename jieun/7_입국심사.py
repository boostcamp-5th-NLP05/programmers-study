def solution(n, times):
    answer = 0

    ## mint 분 안에 모든 사람을 심사할 수 있으면 True, 아니면 False 반환
    def can_do_all(mint):
        cnt = 0 # mint 분 안에 심사할 수 있는 사람 수
        for t in times:
            cnt += mint // t
        return cnt >= n

    lo = -1
    hi = int(1e18) # 최약의 상황: n = 1e9, times=[1e9]

    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if can_do_all(mid):
            hi = mid
        else:
            lo = mid

    answer = hi

    return answer
