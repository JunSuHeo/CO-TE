import sys
from collections import deque

def bfs(graph, root):
    tmp = []
    q = deque([root])

    while q:
        n = q.popleft()
        if n not in tmp:
            tmp.append(n)
            q += graph[n]
    
    return ' '.join(str(i) for i in tmp)

def dfs(graph, root):
    tmp = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in tmp:
            tmp.append(n)
            stack += reversed(graph[n])
    return ' '.join(str(i) for i in tmp)

N, M, V = map(int, sys.stdin.readline().split())

graph = {i:[] for i in range(1, N+1)}
for i in range(M):
    start, end = map(int, sys.stdin.readline().split())

    if start not in graph:
        graph[start] = [end]
    elif end not in graph[start]:
        graph[start].append(end)
    
    if end not in graph:
        graph[end] = [start]
    elif start not in graph[end]:
        graph[end].append(start)
    
for i in graph:
    if i in graph:
        graph[i].sort()

print(dfs(graph, V))
print(bfs(graph, V))