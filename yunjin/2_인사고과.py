# 출처 : https://www.ai-bio.info/programmers/152995
def solution(scores):
    answer = 0
    target_a, target_b = scores[0]
    target_score = target_a + target_b

    # 첫번째 점수에 대해서 내림차순,
    # 첫 번째 점수가 같으면 두 번째 점수에 대해서 오름차순으로 정렬합니다.
    scores.sort(key=lambda x: (-x[0], x[1]))
    maxb = 0

    for a, b in scores:
        if target_a < a and target_b < b:
            return -1

        if b >= maxb: # 근무 태도가 내림차순이고, 동료 평가가 오름차순이므로 동료 평가는 이전의 maxb 보다 크거나 같아야 인센티브를 받을 수 있는 사람임.
            maxb = b
            if a + b > target_score:
                answer += 1

    return answer + 1





def solution(scores):
    answer = 0

    for i in range(len(scores)):
        scores[i] = scores[i] + [i + 1] + [scores[i][0] + scores[i][1]]

    whs = scores[0] # 완호 점수

    # 근무 태도 순으로 정렬
    scores.sort(key=lambda x: x[0])

    new_scores = []

    # 인센티브 못받는 사람 제거하기.
    # 자신보다 근무태도가 높은 사람들 중에서
    for i in range(len(scores)):
        flag = False
        for j in range(i, len(scores)):

            if scores[i][0] == scores[j][0] and scores[i][1] < scores[j][1]: # 근무 태도가 같고, 동료 평가가 높은 사람이 있어도 인센티브 받을 수 있음
                continue

            if scores[i][1] < scores[j][1]:  # 동료 평가가 높은 사람이 있다면 그 사람은 인센티브에서 제외한다. (모두 낮은 경우)
                flag = True
                break

        if not flag:
            new_scores.append(scores[i]) # for문 통과하지 않았다면 인센티브를 모두 낮은 경우가 한번도 없었다는 것이 됨.

    # 점수 역순으로, 사원 번호 오름차순으로 정렬함.
    new_scores.sort(key = lambda x : (-x[3], x[2]))

    # 완호 랭킹
    if whs in new_scores:
        rank = 1
        for i in range(len(new_scores)):
            if new_scores[i][2] == 1:
                answer = rank
                break
            else:
                rank += 1
    else: # 완호가 없다면
        answer = -1

    return answer