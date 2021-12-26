import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, distanceIdx):
    q = []
    heapq.heappush(q, (0, start))

    distanceIdx[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        if distanceIdx[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distanceIdx[i[0]]:
                distanceIdx[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    distanceIdx[0] = 0

N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for i in range(M):
    v1, v2, cost = map(int, input().split())

    graph[v1].append((v2, cost))

dijkstra(X, distance)

arr = []
for i in range(1, N+1):
    distanceIdx = [INF] * (N+1)
    dijkstra(i, distanceIdx)
    toDist = distanceIdx[X]
    fromDist = distance[i]
    arr.append(toDist + fromDist)

print(max(arr))