from collections import deque

# Each letter is a vertex. A1 and A2 distinguish the two A letters.
graph = {
    "A1": ["L", "I"],
    "L": ["A1", "C", "A2"],
    "I": ["A1", "B", "O"],
    "C": ["L", "B"],
    "A2": ["L", "O"],
    "B": ["I", "C"],
    "O": ["I", "A2"]
}


def breadth_first_search(start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []

    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def depth_first_search(start):
    visited = set()
    result = []

    def visit(current):
        visited.add(current)
        result.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return result


def main():
    print("GRAPH - ALICABO")
    print("Vertices:", ", ".join(graph.keys()))
    print("Edges: A1-L, A1-I, L-C, L-A2, I-B, I-O, C-B, A2-O")
    print("BFS:", " - ".join(breadth_first_search("A1")))
    print("DFS:", " - ".join(depth_first_search("A1")))


if __name__ == "__main__":
    main()
