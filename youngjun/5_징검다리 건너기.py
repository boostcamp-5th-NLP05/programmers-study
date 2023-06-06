def solution(stones, k):
    len_stones = len(stones)

    answer = 1e9

    pre = stones[0] #k칸 이후를 볼 때 기준
    cnt = 0 #k칸 이내에 작거나 같은 것들 count
    i = -1 #idx

    while i < len_stones - 1:
        i += 1

        if stones[i] > pre: #기존의 기준보다 클 때
            pre = stones[i]
            cnt = 0

        else:
            cnt += 1
            if cnt >= k:
                if i == len_stones - 1: #감소하면서 끝까지 왔을 때
                    answer = min(answer,max(stones[len_stones-k:]))
                    break

                if stones[i] < stones[i+1]: #계속 같거나 감소할 때
                    answer = min(answer,max(stones[i-k+1:i+1]),max(stones[:k]))
                    #answer = min(answer,max(stones[i-k+1:i+1])) 이렇게 하면 21번만 틀리는데 반례를 못찾겠습니다
                    cnt = 0
                    pre = -1
                    i = i - k #i-k+1부터 다시 반복

    if answer == 1e9: #answer가 바뀌지 않은 경우 (stones의 숫자가 우상향 하거나, k가 len(stones)와 같을 때)
        answer = max(stones[:k])

    return answer