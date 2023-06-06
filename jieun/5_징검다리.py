
def solution(stones, k):
    N = len(stones)
    right = list(range(N+2)) # 왼쪽, 오른쪽 끝 패딩
    left = list(range(N+2))

    def find_right(x):
        if right[x] != x:
            right[x] = find_right(right[x])
        return right[x]
    
    def find_left(x):
        if left[x] != x:
            left[x] = find_left(left[x])
        return left[x]

    def union_right(x, y):
        x = find_right(x)
        y = find_right(y)
        if x > y:
            right[y] = x
        else:
            right[x] = y
            
    def union_left(x, y):
        x = find_left(x)
        y = find_left(y)
        if x < y:
            left[y] = x
        else:
            left[x] = y
    
    q = [(val, idx+1) for idx, val in enumerate(stones)]
    q.sort() # 디딤돌 값 오름차순 정렬
    # print("q:", q)
    last_cnt = 0
    
    for cur_val, cur_idx in q:
        last_cnt = max(last_cnt, cur_val)

        union_left(cur_idx, cur_idx-1)
        union_right(cur_idx, cur_idx+1)

        left_group = find_left(cur_idx)
        right_group = find_right(cur_idx)
        
        # print(f"(val:{cur_val}, idx:{cur_idx}) left_group: {left_group}, right_group:{right_group}")
        
        if right_group - left_group > k:
            break
    
    # last_cnt 번째 친구가 건넌 후 더 이상 징검다리 못 건넌다.
    answer = last_cnt 

    return answer


# stones = [1, 5]
# k = 2

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3

print("sol:", solution(stones, k))
