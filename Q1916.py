import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
dist = [INF] * (N+1)

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        distance, now = heapq.heappop(q)

        if dist[now] < distance:
            continue
        for i in graph[now]:
            cost = distance + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

for i in range(M):
    v1, v2, cost = map(int, input().split())

    graph[v1].append((v2, cost))

start, end = map(int, input().split())

dijkstra(start)

print(dist[end])