def solution(sequence):
    #펄스 수열이 1로 시작할 때
    mul_1 = 1
    sum_1 = 0
    answer_1 = 0
    
    #펄스 수열이 -1로 시작할 때
    mul_2 = -1
    sum_2 = 0
    answer_2 = 0
    
    for i in sequence:
        sum_1 += i * mul_1
        answer_1 = max(answer_1, sum_1)
        if sum_1 <= 0: #누적합이 0 이하일 때 0으로 초기화
            sum_1 = 0
        mul_1 *= -1
        
        sum_2 += i * mul_2
        answer_2 = max(answer_2, sum_2)
        if sum_2 <= 0: #누적합이 0 이하일 때 0으로 초기화
            sum_2 = 0
        mul_2 *= -1
        
    return max(answer_1,answer_2)