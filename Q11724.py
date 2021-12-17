import sys
sys.setrecursionlimit(10**7)

def dfs(root):
    visited[root] = True

    for i in graph[root]:
        if visited[i] == False:
            dfs(i)


N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for i in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())

    graph[v1].append(v2)
    graph[v2].append(v1)

count = 0
for i in range(1, N+1):
    if visited[i] == False:
        count+=1
        dfs(i)

print(count)