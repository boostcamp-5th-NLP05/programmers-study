def solution(scores):
    answer = 1

    target = scores[0]
    sum_target = sum(target)
    scores.sort(key=lambda x: (-x[0], x[1]))

    max_score = 0
    for score in scores:
        
        if target[0] < score[0] and target[1] < score[1]:
            return -1

        if max_score <= score[1]:
            if sum_target < sum(score):
                answer += 1
            max_score = score[1]
            
    return answer