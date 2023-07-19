from collections import deque

def solution(n, cores):
    if n <= len(cores):
        return n
    
    answer = 0
    queue = deque([[] for _ in range(max(cores))])
    
    for i in range(len(cores)):
        queue[cores[i]-1].append((cores[i],i))
    
    n -= len(cores)
    
    while n > 0:
        now = queue.popleft()
        queue.append([])
        
        if now == []:
            continue
            
        for i in now:
            queue[i[0]-1].append((i[0],i[1]))
        
        if len(now) >= n:
            break
        
        n -= len(now)
    
    now.sort(key = lambda x : x[1])
    
    return now[n-1][1] + 1