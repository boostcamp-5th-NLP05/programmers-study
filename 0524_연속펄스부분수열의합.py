def solution(sequence):
    answer = 0
    start_index = 0 # 부분수열 시작 index
    next_false = False # 펄스수열의 다음 부호가 -(False)인지 여부
    answer_list = []
    for i in range(len(sequence)):

        if not next_false: # 펄스수열의 다음 부호가 +면
            answer += sequence[i]
        else:
            answer -= sequence[i]


        if answer < 0: # 펄스수열 뒤집기
            answer = -answer
            next_false = not next_false


        if (i - start_index) %2 == 0: #현재값과 곱할 부호와 첫 index와 곱할 부호가 같을 때
            if next_false and sequence[start_index] >0: # 부호 -일 때 & 처음 값이 +일 때 -> 처음 값 update
                answer += sequence[start_index]
                start_index += 1
            elif (not next_false) and sequence[start_index] <0: #부호 +일 때  & 처음 값이 -일 때 -> 처음 값 update
                answer += sequence[start_index]
                start_index += 1
        else: #현재값과 곱할 부호와 첫 index와 곱할 부호가 다를 때
            if next_false and sequence[start_index] <0: # 부호 -일 때 & 처음 값이 -일 때 -> 처음 값 update
                answer += sequence[start_index]
                start_index += 1
            elif (not next_false) and sequence[start_index] >0: # 부호 +일 때 & 처음 값이 +일 때 -> 처음 값 update
                answer += sequence[start_index]
                start_index += 1 
        next_false = not next_false
        answer_list.append(answer)

    return max(answer_list)



print(solution([2, 3, -6, 1, 3, -1, 2, 4]))