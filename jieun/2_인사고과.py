import heapq


def solution(scores):
    answer = 0
    wanho = tuple(scores[0])
    wanho_sum = sum(wanho)

    scores.sort(reverse=True)  # 내림차순 정렬
    valid = []  # 인센티브 받는 사원들 저장 (-합)

    check = tuple(scores[0])  # 현재 보고 있는 사원보다 근무 태도 점수가 높은 사원 중 동료 평가 점수가 최대인 점수
    next_check = tuple(scores[0])  # 현재 보고 있는 사원과 근무 태도 점수가 크거나 같은 사원 중 동료 평가 점수가 최대인 점수

    ## 인센티브 받는 사원 찾기
    for i in range(len(scores)):

        # 근무 태도 점수가 바뀌면 next_check와 check 중 동료 평가 점수가 높은 것을 check 조건으로 갱신
        if scores[i][0] != scores[i - 1][0]:
            if check[1] < next_check[1]:
                check = next_check

        # check 조건보다 점수가 다 낮아서 인센티브 못 받음
        if scores[i][0] < check[0] and scores[i][1] < check[1]:
            if tuple(scores[i]) == wanho:
                answer = -1
                break
            else:
                continue

        # 인센티브 받음
        heapq.heappush(valid, -sum(scores[i]))

        # 현재 점수와 next_check 점수 중 동료 평가 점수가 높은 것으로 next_check 갱신
        if next_check[1] < scores[i][1]:
            next_check = tuple(scores[i])

    ## 완호가 인센티브 못 받았으면
    if answer == -1:
        return answer

    rank = 1  # 현재 보는 석차
    cnt = 0  # 현재 보는 석차를 가지는 사원 수
    rank_sum = -1  # 현재 보는 석차에 해당하는 점수 합

    ## 석차 구하기
    while valid:
        cur_sum = heapq.heappop(valid)
        if cur_sum == rank_sum:  # 동일 석차
            cnt += 1
        else:
            rank += cnt
            cnt = 1
            rank_sum = cur_sum

        if -cur_sum == wanho_sum:
            answer = rank
            break

    return answer
