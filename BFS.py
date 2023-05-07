
from collections import deque

def bfs(graph, v, visited):
    q = deque([v])    
    visited[v] = True;

    while q:
        v = q.popleft()
        print(v, end=" ")
        for u in graph[v]:
            q.append(u)
            visited[u] = True

