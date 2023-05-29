def solution(scores):
    wanho0 = scores[0][0] #완호의 점수 따로 저장
    wanho1 = scores[0][1]
    wanho_num = 1
    scores = scores[1:]
    scores.sort()
    wanho_incen = 1 #완호의 인센티브 획득 여부 판단

    for i in range(len(scores)-1):
        notcontain = False
        for j in range(i+1,len(scores)):
            if scores[i][0] < scores[j][0] and scores[i][1] < scores[j][1]: 
                notcontain = True #둘다 작은 경우가 있으면 인센티브를 받을 수 없다
                break
        if scores[i][0] + scores[i][1] > wanho0 + wanho1 and notcontain == False:
            wanho_num += 1 #완호 점수 update

        if scores[i][0] > wanho0 and scores[i][1] > wanho1:
            wanho_incen += 1 #완호의 인센티브여부 update
    
    if scores[-1][0] + scores[-1][1] > wanho0 + wanho1: #가장 큰 점수도 체크
            wanho_num += 1
    if wanho_incen == len(scores):
         return -1
    
    return wanho_num

print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))