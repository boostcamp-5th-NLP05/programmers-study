def solution(A, B):
    answer = 0
    A.sort(reverse = True)
    B.sort(reverse = True)
    for i in range(len(A)):
        if B[0] > A[i]: # 현재 A의 가장 큰 값보다 B가 크면 B 1점 획득
            answer += 1
            B.pop(0)
        else:
            B.pop() #B의 가장 작은 값을 제외하여 최대한 많은 승점 획득

    return answer


print(solution([5,1,3,7], [2,2,6,8]))


