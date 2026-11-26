# Assessment 3.6: DFS Methods in Tree
# Tree built from: First Name (JHON) + Last Name (ALICABO)
# Repeated letters are numbered in name order: O1, O2 and A1, A2.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(root):
    """Root -> Left -> Right"""
    if root is None:
        return []

    result = [root.value]
    result.extend(preorder(root.left))
    result.extend(preorder(root.right))
    return result


def inorder(root):
    """Left -> Root -> Right"""
    if root is None:
        return []

    result = inorder(root.left)
    result.append(root.value)
    result.extend(inorder(root.right))
    return result


def postorder(root):
    """Left -> Right -> Root"""
    if root is None:
        return []

    result = postorder(root.left)
    result.extend(postorder(root.right))
    result.append(root.value)
    return result


def create_name_tree():
    root = Node("J")

    root.left = Node("H")
    root.right = Node("O1")

    root.left.left = Node("N")
    root.left.right = Node("A1")
    root.right.left = Node("L")
    root.right.right = Node("I")

    root.left.left.left = Node("C")
    root.left.left.right = Node("A2")
    root.left.right.left = Node("B")
    root.left.right.right = Node("O2")

    return root


def main():
    root = create_name_tree()

    print("DFS METHODS IN TREE - JHON ALICABO")
    print("Preorder  (Root-Left-Right):", " - ".join(preorder(root)))
    print("Inorder   (Left-Root-Right):", " - ".join(inorder(root)))
    print("Postorder (Left-Right-Root):", " - ".join(postorder(root)))


if __name__ == "__main__":
    main()