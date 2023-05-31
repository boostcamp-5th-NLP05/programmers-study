from collections import deque


def solution(A, B):
    answer = 0

    total = []
    for num in A:
        total.append((num, "A"))
    for num in B:
        total.append((num, "B"))
    total.sort()

    # 지금까지 나온 A팀의 값을 저장해둘 큐
    q_A = deque()

    for val, team in total:
        if team == "A":
            q_A.append(val)

        else:
            if q_A:
                # 여기서 val_A는 자동으로 지금까지 나온 A팀의 값 중 가장 작은 값
                val_A = q_A.popleft()
                if val_A < val:
                    answer += 1

                # 같은 값이 나오면 뒤에 나올 B보다 작을 수도 있으니 재사용
                if val_A == val:
                    q_A.appendleft(val)

    return answer
