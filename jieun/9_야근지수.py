from collections import Counter


def solution(n, works):
    answer = 0
    counter = Counter(works)
    counter = [(0, 0)] + sorted(list(counter.items()))  # (작업량, 개수)
    cur = counter.pop()  # (최대 작업량, 개수)
    while counter:
        nxt = counter.pop()

        # cur의 모든 일의 작업량을 nxt의 작업량으로 감소시키기 위해 필요한 시간
        full = (cur[0] - nxt[0]) * cur[1]

        if full <= n:  # 시간 충분
            n -= full  # 사용한 시간 빼기
            cur = (nxt[0], cur[1] + nxt[1])  # (최대 작업량, 개수) 갱신
        else:  # 시간 부족
            sub = n // cur[1]  # cur의 모든 일에 대해 감소시킬 수 있는 작업량
            left = n % cur[1]  # 감소시키고 남을 시간. 또는, 작업량을 1만큼 더 감소시킬 수 있는 일 개수
            tmp1 = (cur[0] - sub, cur[1] - left)  # (최대 작업량, 개수) 갱신
            tmp2 = (tmp1[0] - 1, left)  # 남은 시간을 사용해서 가능한 일에서 작업량 1만큼씩 빼기
            counter.extend([tmp1, tmp2, nxt])
            break

    # 야근 피로도 계산
    for v, c in counter:
        answer += v * v * c

    return answer
