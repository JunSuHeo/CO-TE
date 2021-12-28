import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())

graph = [[]for _ in range(N+1)]
distance = [INF] * (N+1)

for i in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append((v2, 1))
    graph[v2].append((v1, 1))

def dijkstra(start):
    distance = [INF] * (N+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                heapq.heappush(q, (cost, i[0]))
                distance[i[0]] = cost
    
    del distance[start]

    return sum(distance[1:])

answer = (INF, 0)
for i in range(1, N+1):
    kevin = dijkstra(i)
    if answer[0] > kevin:
        answer = (kevin, i)

print(answer[1])