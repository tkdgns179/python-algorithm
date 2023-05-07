from enum import Enum
from collections import deque

""" 
예제 1
4 5
00110
00011
11111
00000 

예제 2
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
"""
n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))




print(graph)

class Direction(Enum):
    UP = (0, 1)
    DOWN = (0, -1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


# 튜플 v 에서 BFS 시작
def bfs(graph, v) -> int:
    if graph[v[1]][v[0]] != 0:
        return 0
    q = deque()
    q.append(v)
    graph[v[1]][v[0]] = 1

    while q:
        v: tuple[int, int] = q.popleft()
        x, y = v
        # print(f"({x}, {y}) 시작")

        
        # 상하좌우 방문
        for direction in Direction:
            dx, dy = direction.value;
            # print(f"dx = {dx}, dy = {dy}")
            _x, _y = (x + dx, y + dy);
            if (_x >= 0 and _x < m) and (_y >= 0 and _y < n) and (graph[_y][_x] != 1):
                q.append((_x, _y))
                graph[_y][_x] = 1

    # 아이스 음료수 하나 
    return 1

iced_drink = 0;

for i in range(n):
    for j in range(m):
        iced_drink += bfs(graph, (j, i))
        
print(graph, iced_drink)


