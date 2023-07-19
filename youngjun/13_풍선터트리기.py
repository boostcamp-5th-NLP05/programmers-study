def solution(a):
    
    if len(a) <= 2:
        return len(a)
    
    answer = 2 #양쪽 끝 풍선은 무조건 남을 수 있기 때문에
    
    left = a[0]
    right = a[-1]
    left_list = []
    right_list = []
    
    for i in range(1,len(a)-1):
        left_list.append(left) #앞에서 부터 가장 작은 왼쪽 원소 저장
        left = min(left,a[i]) 
        
        right_list.append(right) #뒤에서 부터 가장 작은 오른쪽 원소 저장
        right = min(right,a[-1-i]) 
    
    for i in range(1,len(a)-1):
        if max(a[i],right_list[-i],left_list[i-1]) != a[i]: #a[i]와 a[i]기준 왼쪽 최소, 오른쪽 최소 비교
            answer +=1

    return answer