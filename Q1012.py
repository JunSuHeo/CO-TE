import sys
from collections import deque

def bfs(graph, root):
    q = deque([root])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        x, y = q.popleft()
        for i in range(4):
            moveX = x + dx[i]
            moveY = y + dy[i]

            if 0 <= moveX < N and 0 <= moveY < M and visited[moveX][moveY] == False and graph[moveX][moveY] == 1:
                visited[moveX][moveY] = True
                q.append([moveX, moveY])

T = int(sys.stdin.readline())

for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for j in range(K):
        v1, v2 = map(int, sys.stdin.readline().split())
        graph[v2][v1] = 1
    
    cnt = 0
    for j in range(N):
        for k in range(M):
            if graph[j][k] == 1 and visited[j][k] == False:
                root = [j, k]
                bfs(graph, root)
                cnt += 1
    
    print(cnt)