import sys
import heapq

input = sys.stdin.readline
INF = int(1e8 * 5)

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]


for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start, end):
    distance = [INF] * (N+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist < distance[now]:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                heapq.heappush(q, (cost, i[0]))
                distance[i[0]] = cost
    
    return distance[end]

path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

if path1 >= INF and path2 >= INF:
    print(-1)
else:
    print(min(path1, path2))