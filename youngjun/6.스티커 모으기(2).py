def solution(sticker):
    answer = 0
    n = len(sticker)
    
    if n == 1:
        return sticker[0]
    
    dp = [0 for _ in range(n)] #첫번째  스티커를 사용하는 경우
    for i in range(0,n-1):
        dp[i] = max(dp[i-2]+sticker[i],dp[i-1])
        
    dp2 = [0 for _ in range(n)]
    for i in range(1,n): #첫번째 스티커를 사용하지 않는 경우
        dp2[i] = max(dp2[i-2]+sticker[i],dp2[i-1])
        
    answer = max(dp[-2],dp2[-1])

    return answer

