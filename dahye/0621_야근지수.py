def solution(n, works):
    works.sort(reverse = True) # 내림차순 정렬
    temp_min = min(works)
    while True:
        if temp_min < 0:
            return 0
        temp = [works[w]- temp_min for w in range(len(works))]
        print(temp, temp_min)
        if sum(temp) == n:
            break
        elif sum(temp) < n:
            temp_min -= 1
        else:
            for i in range(sum(temp)-n):
                temp[i] = temp[i]-1
            break
    
    temp_answer = [(works[w] - temp[w])**2 for w in range(len(works))]
    answer = sum(temp_answer)

    return answer


print(solution(3,[1,1]))