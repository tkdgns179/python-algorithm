
# 스택으로 구현한 DFS
def dfs(graph, v, visited):
    s = []

    # 시작 정점 초기화
    visited[v] = True
    s.append(v)
    print(v, end = " ")

    while s:
        
        # 스택의 top 값 인덱싱
        top = s[-1];
        # print(stack, graph[top]);

        # 간선 순회 후, 방문하지 않았다면 해당 정점을 스택에 넣고 방문처리
        for u in graph[top]:
            if not visited[u]:
                s.append(u)
                visited[u] = True
                print(u, end = " ")
                break

        # 스택이 그대로라면 pop하고 while 반복문 루프
        if top == s[-1]:
            s.pop();
    
        

# 무방향 그래프
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 방문리스트
visited = [False]*9

dfs(graph, 1, visited);
# 예상 결과 1 2 7 6 8 3 4 5
