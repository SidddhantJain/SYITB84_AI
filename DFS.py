graph= {'2':['4','6'],
        '4': ['1'],
        '6':['3','9'],
        '3':['1'],
        '1': [],
        '9': []}
visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Following is the Depth-First Search")
dfs(visited, graph, '5')