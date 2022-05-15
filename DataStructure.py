class Node:
    # if color = 0 -> red
    # if color = 1--> black
    def __init__(self, key):  # Constructor
        self.key = key  # Node needs a key to be initialized
        self.parent = None
        self.right = None
        self.left = None
        self.color = 0


class RedBlackTree:
    def __init__(self):  # Constructor
        self.nil = Node(None)
        self.nil.color = 1  # The root and the nil are black
        self.root = self.nil
        self.number_of_nodes = 0

    def search(self, key):
        node = self.root

        while node != self.nil:  # as long as we didn't reach the end of the tree
            if node.key == key:
                return True
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return False

    def insert(self, key):
        newNode = Node(str(key).lower())
        newNode.left = self.nil
        newNode.right = self.nil
        node = self.root
        parent = None  # TBD

        while node != self.nil:  # Find the appropriate parent
            parent = node
            if newNode.key < node.key:
                node = node.left
            else:
                node = node.right
        newNode.parent = parent

        if parent is None:  # Inserted node is the first node
            newNode.color = 1
            self.root = newNode
            self.number_of_nodes += 1
            return
        elif newNode.key < parent.key:
            parent.left = newNode
        else:
            parent.right = newNode

        if newNode.parent.parent is None:  # Parent is the root
            self.number_of_nodes += 1
            return

        self.insertFix(newNode)  # Handle cases
        self.number_of_nodes += 1

    # This method handles cases of RB-tree insertions
    def insertFix(self, newNode):
        while newNode != self.root and newNode.parent.color == 0:  # Loop until we reach the root or parent is black

            parentIsLeft = False  # Parent is considered left child by default

            # Assign uncle to appropriate node
            if newNode.parent == newNode.parent.parent.left:
                uncle = newNode.parent.parent.right
                parentIsLeft = True
            else:
                uncle = newNode.parent.parent.left

            # Case 1: Uncle is red -> Reverse colors of uncle, parent and grandparent
            if uncle.color == 0:
                newNode.parent.color = 1
                uncle.color = 1
                newNode.parent.parent.color = 0
                newNode = newNode.parent.parent

            # Case 2: Uncle is black -> check triangular or linear and rotate accordingly
            else:
                # Left-right condition (triangular)
                if parentIsLeft and newNode == newNode.parent.right:
                    newNode = newNode.parent  # Take care as we made the new node the parent
                    self.leftRotate(newNode)
                # Right-Left condition (triangular)
                elif not parentIsLeft and newNode == newNode.parent.left:
                    newNode = newNode.parent
                    self.rightRotate(newNode)
                # Left-left condition (linear)
                if parentIsLeft:
                    newNode.parent.color = 1  # the new parent
                    newNode.parent.parent.color = 0  # the new grandparent will be red
                    self.rightRotate(newNode.parent.parent)
                # Right-right condition (linear)
                else:
                    newNode.parent.color = 1
                    newNode.parent.parent.color = 0
                    self.leftRotate(newNode.parent.parent)

        self.root.color = 1  # Set root to black

    def leftRotate(self, node):
        """
                node              y
                  \     =>      /  \
                    y         node  d
                  /  \           \
                c     d           c
                """
        y = node.right
        node.right = y.left  # connect node to c
        if y.left != self.nil:  # connect c to node
            y.left.parent = node

        y.parent = node.parent  # connect y to node's parent

        if node.parent is None:  # connect node's parent to y
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y

        y.left = node  # connect y to node
        node.parent = y  # connect node to y

    def rightRotate(self, node):
        """
        node                    y
       /   \        =>        /   \
      y                     c    node
    /   \                        /
   c     d                      d
        """
        y = node.left
        node.left = y.right  # connect node to d
        if y.right != self.nil:  # connect d to node
            y.right.parent = node
        y.parent = node.parent  # connect y to node's parent

        if node.parent is None:  # connect b parent to a's parent
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y

        y.right = node  # connect y to node
        node.parent = y  # connect node to y

    # This method returns the height of the tree
    def heightOfTree(self, node, sumval):
        if node is self.nil:
            return sumval
        return max(self.heightOfTree(node.left, sumval + 1), self.heightOfTree(node.right, sumval + 1))

    # This method returns the black-height of the tree
    def getBlackHeight(self):
        node = self.root
        bh = 0
        while node is not self.nil:
            node = node.left
            if node.color == 1:
                bh += 1
        return bh

    # Function to print used in debugging
    def __printCall(self, node, indent, last):
        if node != self.nil:
            print(indent, end=' ')  # the default end character is new line
            if last:
                print("R----", end=' ')
                indent += "     "
            else:
                print("L----", end=' ')
                indent += "|    "

            s_color = "RED" if node.color == 0 else "BLACK"
            print(str(node.key) + "(" + s_color + ")")
            self.__printCall(node.left, indent, False)
            self.__printCall(node.right, indent, True)

    # Function to call print
    def print_tree(self):
        self.__printCall(self.root, "", True)


"""
tree = RedBlackTree()
tree.insert('a')
tree.insert('b')
tree.insert('e')
tree.insert('d')
tree.insert('c')
tree.insert('f')
tree.insert('g')
tree.insert('h')
tree.insert('i')
tree.insert('j')
tree.print_tree()
print(tree.heightOfTree(tree.root, 0))
print(tree.number_of_nodes)
print(tree.search('q'))
print(tree.getBlackHeight())
"""
