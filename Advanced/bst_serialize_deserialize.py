index = 0
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    @staticmethod
    def serialize(root, output):
        if not root:
            output.append('#')
            return
        output.append(root.value)
        Node.serialize(root.left, output)
        Node.serialize(root.right, output)
        return output
    @staticmethod
    def deserialize(source):
        global index
        if source[index] == '#':
            index += 1
            return None
        value = source[index]
        index += 1
        left = Node.deserialize(source)
        right = Node.deserialize(source)
        return Node(value, left, right)

def printPreorder(root):
 
    if root:
 
        # First print the data of node
        print(root.value),
 
        # Then recur on left child
        printPreorder(root.left)
 
        # Finally recur on right child
        printPreorder(root.right)

if __name__ == "__main__":
  #  root = Node('a', Node('b', None, None), Node('c', Node('e', Node('g', None, None), None), Node('f', None, None)))
    root = Node(1)
    root.left      = Node(2)
    root.right     = Node(3)
    root.left.left  = Node(4)
    root.left.right  = Node(5)
    result = []
    Node.serialize(root, result)
    print result
    new_root = Node.deserialize(result)
    printPreorder(new_root)
    print
    result2 = []
    Node.serialize(new_root, result2)
    print result2

