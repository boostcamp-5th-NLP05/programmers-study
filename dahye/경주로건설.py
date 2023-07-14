from collections import deque
import copy

def solution(board): #bfs
    n = len(board)
    _visited = [[False for _ in range(n)]for _ in range(n)]
    _visited[0][0] = True
    queue = deque() # 현재 x좌표, y좌표, 비용, 방향(상:3,하:2,좌:1,우:0)
    queue.append((0,0,0,0,_visited)) # 두 방향으로 시작
    queue.append((0,0,0,2,_visited))
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    answer_list = []
    
    while queue :
        x,y,temp,_dir,visited_temp = queue.popleft()
        visited = copy.deepcopy(visited_temp)
        for i in range(4): #상하좌우
            nx = x+dx[i]
            ny = y+dy[i]
            if not (nx>=n or nx<0 or ny>=n or ny<0): #범위일 때
                if board[ny][nx] == 0 and visited[ny][nx] == False: # 벽이 없는 곳 and 방문한적 없는 곳
                    if ((i == 1 or i == 0) and (_dir == 1 or _dir == 0)) or (i == 2 or i == 3) and (_dir == 2 or _dir == 3): # 방향이 같으면
                        add = 100 # 직선도로
                    else: #코너
                        add = 600
                    visited[ny][nx] = True
                    queue.append((nx,ny,temp+add,i,visited))

                    if (nx == n-1) and (ny == n-1):
                        answer_list.append(temp+add)
            

    return min(answer_list)

print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))