from bisect import bisect_right
def solution(A, B):
    answer = 0
    B.sort()
    for i in A:
        tmp = bisect_right(B,i)
        if tmp == len(B):
            del B[0]
        else:
            del B[tmp]
            answer += 1
    return answer