from collections import deque

def solution(board): #dfs
    n = len(board)
    min_cost = int(1e9)
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    answer_list = []
    for dd in [0,2]: # 두 방향으로 시작
        queue = deque() # 현재 x좌표, y좌표, 비용, 방향(상:3,하:2,좌:1,우:0)
        queue.append((0,0,0,dd)) 
        visited = [[min_cost for _ in range(n)] for _ in range(n)]
        visited[0][0] = 0
        while queue :
            x,y,temp,_dir = queue.popleft()
            for i in range(4): #상하좌우
                nx = x+dx[i]
                ny = y+dy[i]
                if not (nx>=n or nx<0 or ny>=n or ny<0): #범위일 때
                    if board[ny][nx] == 0: # 벽이 없는 곳
                        if i == _dir: # 방향이 같으면
                            add = 100 # 직선도로
                        else: #코너
                            add = 600
                        if temp+add <= visited[ny][nx] + 400:
                            visited[ny][nx] = temp+add
                            #visited[ny][nx] = min(temp+add, visited[ny][nx])
                            queue.append((nx,ny,temp+add,i))

                        if (nx == n-1) and (ny == n-1):
                            answer_list.append(temp+add)

    return min(answer_list)

print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))