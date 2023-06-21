def solution(n, works):
    answer = 0
    
    if sum(works) <= n:
        return 0
    works.sort(reverse=True) #내림차순 정렬
    
    for i in range(len(works)-1):
        if n <= 0:
            break

        tmp = works[i] - works[i+1] #다음에 올 숫자랑 비교

        if tmp == 0: #다음 숫자랑 같다면 다음
            continue

        else:
            if n > (i+1) * tmp: #n이 (지금까지 본 숫자 개수) * (다음 숫자와의 차이) 보다 클 때
                for j in range(i+1):
                    works[j] -= tmp
                n -= (i+1) * tmp
                
            else: #작다면
                for j in range(i+1):
                    works[j] -= n//(i+1)
                for j in range(n % (i+1)):
                    works[j] -= 1
                n = 0
                break

    if n > 0: #모든 숫자가 같아지고, n이 남아있을 때
        for j in range(len(works)):
            works[j] -= n//len(works)
        for j in range(n % len(works)):
            works[j] -= 1

    for i in works:
        answer += i**2

    return answer