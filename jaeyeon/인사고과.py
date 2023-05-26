def solution(scores):
    answer = 1
    target = scores[0]

    scores.sort(key=lambda x: (-x[0], x[1]))

    cur_max = 0
    for score in scores:
        # 영호가 인센티브를 못 받는 케이스
        if target[0] < score[0] and target[1] < score[1]:
            return -1

        # 영호보다 앞 순위에 있는 사람들 구하기
        if cur_max <= score[1]:  # 인센티브를 못 받는 사람을 거르는 부분
            if sum(target) < sum(score):
                answer += 1
            cur_max = score[1]
    return answer
