def solution(sequence):
    answer_list1 = [sequence[0] if sequence[0]>0 else 0] #펄스수열이 1부터 시작하는 경우의 누적합
    answer_list2 = [-sequence[0] if -sequence[0]>0 else 0] #펄스수열이 -1부터 시작하는 경우의 누적합
    temp = -1
    for i in range(1,len(sequence)):
        if answer_list1[i-1] + sequence[i]*temp>0:
            answer_list1.append(answer_list1[i-1] + sequence[i]*temp)
        else:
            answer_list1.append(0) # 0보다 작으면 누적합 초기화

        if answer_list2[i-1] + sequence[i]*temp*(-1)>0:
            answer_list2.append(answer_list2[i-1] + sequence[i]*temp*(-1))
        else:
            answer_list2.append(0) # 0보다 작으면 누적합 초기화
        temp = temp*(-1) #펄스수열 바꾸기
        print(answer_list1)
        print(answer_list2)


    return max(max(answer_list1),max(answer_list2))



print(solution([2, 3, -6, 1, 3, -1, 2, 4]))