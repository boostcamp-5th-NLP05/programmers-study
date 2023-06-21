def solution(n, works):
    # n의 작업으로 야근을 안 해도 되면 바로 return
    if sum(works) <= n:
        return 0

    max_val = max(works)
    # max_val+1 길이의 배열 생성
    val_list = [0] * (max_val + 1)

    # 값 리스트 업데이트
    for val in works:
        val_list[val] += 1

    # 뒤에서부터 순회하면서 시간이 오래 걸리는 일부터 쳐내기
    for idx in range(max_val, 0, -1):
        if val_list[idx] != 0:
            if val_list[idx] <= n:
                n -= val_list[idx]
                val_list[idx - 1] += val_list[idx]
                val_list[idx] = 0
                if n == 0:
                    break
            else:
                val_list[idx] -= n
                val_list[idx - 1] += n
                break

    # 남은 일 계산하기
    answer = 0
    for idx, val in enumerate(val_list):
        if val != 0:
            answer += val * idx * idx

    return answer
