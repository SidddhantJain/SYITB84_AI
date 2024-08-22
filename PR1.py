class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def createNode(data):
    return Node(data)


def addEdge(adjList, u, v):
    newNode = createNode(v)
    newNode.next = adjList[u]
    adjList[u] = newNode


def bfs(adjList, vertices, startNode, visited):
    queue = [0] * vertices
    front, rear = 0, 0

    visited[startNode] = 1
    queue[rear] = startNode
    rear += 1

    while front != rear:
        currentNode = queue[front]
        front += 1
        print(currentNode, end=" ")

        neighbors = []
        temp = adjList[currentNode]
        while temp is not None:
            if not visited[temp.data]:
                neighbors.append(temp.data)
            temp = temp.next

        for neighbor in sorted(neighbors):
            if not visited[neighbor]:
                visited[neighbor] = 1
                queue[rear] = neighbor
                rear += 1


def bfs_find(adjList, vertices, startNode, visited, goal):
    queue = [0] * vertices
    front, rear = 0, 0

    visited[startNode] = 1
    queue[rear] = startNode
    rear += 1

    while front != rear:
        currentNode = queue[front]
        front += 1
        print(currentNode, end=" ")

        if currentNode == goal:
            print("\nELEMENT FOUND")
            return

        neighbors = []
        temp = adjList[currentNode]
        while temp is not None:
            if not visited[temp.data]:
                neighbors.append(temp.data)
            temp = temp.next

        for neighbor in sorted(neighbors):
            if not visited[neighbor]:
                visited[neighbor] = 1
                queue[rear] = neighbor
                rear += 1

    print("\nELEMENT NOT FOUND")


def main():
    vertices = int(input("Enter the number of vertices: "))
    adjList = [None] * vertices

    numEdges = int(input("Enter the number of edges: "))

    for _ in range(numEdges):
        val1 = int(input("Enter the initial node: "))
        val2 = int(input("Enter the final node for the edge: "))
        addEdge(adjList, val1, val2)

    visited = [0] * vertices

    startNode = int(input("Enter the starting node for BFS: "))
    print(f"Breadth First Traversal starting from vertex {startNode}: ", end=" ")
    bfs(adjList, vertices, startNode, visited)

    goal = int(input("\nEnter the node to search for: "))
    visited = [0] * vertices  # Reset visited for the search
    print(f"Searching for element {goal} starting from vertex {startNode}: ", end=" ")
    bfs_find(adjList, vertices, startNode, visited, goal)


if __name__ == "__main__":
    main()
