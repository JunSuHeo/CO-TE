import sys
from collections import deque

def bfs(tomato):
    while q:
        x, y = q.popleft()

        for i in range(4):
            moveX, moveY = x + dx[i], y + dy[i]
            if 0 <= moveX < N and 0 <= moveY < M and tomato[moveX][moveY] == 0:
                tomato[moveX][moveY] = tomato[x][y] + 1
                q.append([moveX, moveY])

M, N = map(int, sys.stdin.readline().split())

tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque([])

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append([i, j])

bfs(tomato)
result = 0

for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    
    result = max(result, max(i))

print(result - 1) 

