def solution(A, B):

    answer = 0

    # 내림차순 정렬
    A.sort(reverse=True)
    B.sort(reverse=True)

    b_idx = 0

    for a_idx in range(len(A)):

        # B가 크면 A, B 둘다 인덱스 증가
        if B[b_idx] > A[a_idx]:
            answer += 1 # 승점 획득
            b_idx += 1

        # B가 작은 경우
        else:

            # B의 가장 작은 수를
            tmp = B.pop()

            # 넣어줘서 가장 작은 패로 패배를 하도록 함
            B.insert(b_idx, tmp)
            b_idx += 1

    return answer