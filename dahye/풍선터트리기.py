# def solution(a): # 시간초과 풀이
#     answer = 0
#     for i in range(len(a)):
#         if a[i] != min(a[i:]) and min(a[:i+1]) != a[i]: # 양옆의 가장 최솟값이 자신이 아니어야 함
#             answer += 1
#     return len(a) - answer

def solution(a):
    answer = 0
    temp_min_left = a[0]
    min_left = []
    temp_min_right = a[-1]
    min_right = []

    for i in range(len(a)):
        if a[i] < temp_min_left:
            temp_min_left = a[i]
        min_left.append(temp_min_left)
        if a[len(a)-i-1] < temp_min_right:
            temp_min_right = a[len(a)-i-1]
        min_right.append(temp_min_right)
    for j in range(len(a)):
        if a[j] <= min_right[len(a)-1-j] or a[j] <= min_left[j]:
            answer += 1
    return answer


print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))