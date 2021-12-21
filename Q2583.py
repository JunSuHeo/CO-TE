import sys
from collections import deque

def bfs(root):
    q = deque([root])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    cnt = 0

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            moveX = x + dx[i]
            moveY = y + dy[i]

            if 0 <= moveX < M and 0 <= moveY < N and arr[moveX][moveY] == 0 and visited[moveX][moveY] == False:
                visited[moveX][moveY] = True
                q.append([moveX, moveY])
                cnt += 1

    return cnt

M, N, K = map(int, sys.stdin.readline().split())

arr = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]

for i in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    for j in range(x1, x2):
        for k in range(y1, y2):
            arr[k][j] = 1

result = []

for i in range(M):
    for j in range(N):
        if arr[i][j] == 0 and visited[i][j] == False:
            start = [i, j]
            tmp = bfs(start)
            if tmp == 0:
                tmp += 1
            result.append(tmp)

result.sort()

print(len(result))
for i in range(len(result)):
    print(result[i], end=" ")