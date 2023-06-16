from collections import deque
def solution(board):
    answer = 0
    move = [(0,1,0),(0,-1,0),(1,0,1),(-1,0,1)]#동,서,남,북 가로 = 0 세로 = 1
    
    inf = 1e9
    N = len(board)
    map_ = [[inf for _ in range(N)] for _ in range(N)]
    map_[0][0] = 0
    
    queue = deque()
    
    queue.append([0,0,-1,-500]) #r,c,방향,비용(처음 방향이 어디로 가던 코너라 가정)
    while queue:
        r,c, di,cost = queue.popleft()
        
        if r == N-1 and c == N-1:
            continue

        for i in move:
            nr = r + i[0]
            nc = c + i[1]
            if nr in [-1,N] or nc in [-1,N]:
                continue
            if board[nr][nc] == 1:
                continue

            else:
                if di != i[2]: #코너일 경우
                    ncost = cost + 600
                else:
                    ncost = cost + 100
                
                if ncost <= map_[nr][nc] + 400:#500원 넘게 차이나는 경우 결국 작아지는 경우가 없기 때문에
                    map_[nr][nc] = min(ncost,map_[nr][nc])
                    queue.append([nr,nc,i[2],ncost])
    return map_[N-1][N-1]