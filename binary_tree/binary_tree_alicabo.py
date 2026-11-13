class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def breadth_first_search(root):
    if root is None:
        return []

    queue = [root]
    result = []

    while queue:
        current = queue.pop(0)
        result.append(current.value)

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

    return result


def depth_first_search(root):
    if root is None:
        return []

    result = [root.value]
    result.extend(depth_first_search(root.left))
    result.extend(depth_first_search(root.right))
    return result


def create_alicabo_tree():
    root = Node("A")

    root.left = Node("L")
    root.right = Node("I")

    root.left.left = Node("C")
    root.left.right = Node("A2")

    root.right.left = Node("B")
    root.right.right = Node("O")

    return root


def main():
    root = create_alicabo_tree()

    print("BINARY TREE - ALICABO")
    print("BFS (level order):", " - ".join(breadth_first_search(root)))
    print("DFS (preorder):", " - ".join(depth_first_search(root)))


if __name__ == "__main__":
    main()
