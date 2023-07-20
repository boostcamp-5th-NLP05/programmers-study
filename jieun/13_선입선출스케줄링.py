import heapq


def solution(n, cores):
    # 시간 초과

    que = [(0, idx) for idx in range(len(cores))]  # (끝 시각, 코어 번호)

    while n > 0:
        end, core = heapq.heappop(que)
        heapq.heappush(que, (end + cores[core], core))
        n -= 1

    answer = core + 1
    return answer


### 밑은 미완성 풀이 ###


def find_works(n, idx, cores):
    time = cores[idx]
    # idx번째 코어가 m 개의 일을 끝냈을 때, works = sum{m*time // cores[i]}
    # works >= n 인 최소 works 구하기

    # if m == 1
    # w = idx + 1

    def total_works_in_cycle(idx, work):
        if work == 0:
            return 0

        res = 0
        cycle = work * time
        for i, t in enumerate(cores):
            q = cycle // t
            r = cycle % t
            if r == 0 and i > idx:
                res += max(0, q - 1)
            else:
                res += q
        return res

    # m에 대해 이분탐색
    # works >= n 인 최소 works
    # FFTT
    lo = 0
    hi = n + 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        w = total_works_in_cycle(idx, mid)
        if w >= n:
            hi = mid
        else:
            lo = mid

    w = total_works_in_cycle(idx, hi)

    print(f"cores[{idx}]={time} finished {hi} works: total {w} works / {n}")

    return w


def solution2(n, cores):
    # solution2 보다 시간 더 걸림
    answer = None

    if n <= len(cores):
        return n

    n -= len(cores)  # 시각 0에서 모든 작업 시작

    # for idx in range(len(cores)):
    #     # idx 번째에서 전체 작업이 끝난다고 가정할 때, 처리한 전체 일 개수
    #     works = find_works(n, idx, cores)
    #     if n == works:
    #         answer = idx+1
    #         break

    # 시간 내림, 번호 내림
    # idx 대해 이분탐색
    # works <= n
    # TTFF

    sorted_cores = [(idx, val) for idx, val in enumerate(cores)]
    sorted_cores.sort(key=lambda x: (-x[1], -x[0]))
    lo = 0
    hi = len(cores)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        works = find_works(n, mid, cores)
        if works <= n:
            lo = mid
        else:
            hi = mid

    answer = lo + 1

    return answer


if __name__ == "__main__":
    n = 6
    cores = [1, 2, 3]
    result = 2
    print(solution(n, cores))
