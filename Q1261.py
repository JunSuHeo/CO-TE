import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

arr = []

for i in range(M):
    arr.append(input())

distance = [[-1] * (N) for _ in range(M)]
distance[0][0] = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()
q.append([0, 0])

while q:
    x, y = q.popleft()

    for i in range(4):
        moveX, moveY = x + dx[i], y + dy[i]

        if 0 <= moveX < N and 0 <= moveY < M and distance[moveY][moveX] == -1:
            if arr[moveY][moveX] == '0':
                q.appendleft([moveX, moveY])
                distance[moveY][moveX] = distance[y][x]
            elif arr[moveY][moveX] == '1':
                q.append([moveX, moveY])
                distance[moveY][moveX] = distance[y][x] + 1

print(distance[M-1][N-1])