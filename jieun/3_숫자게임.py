def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    a = 0
    b = 0
    n = len(A)
    while a < n and b < n:
        if A[a] < B[b]:
            answer += 1
            a += 1
            b += 1
        else:
            b += 1

    return answer
