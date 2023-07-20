def solution(a):
    answer = 0

    # min_idx = a.index(min(a))
    a.sort()
    x = a[len(a) // 2]
    print(x)

    for i in range(len(a)):
        if a[i] <= x:
            answer += 1

    return answer