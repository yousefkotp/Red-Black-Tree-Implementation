class Node:
    #if color = 0 then red, if 1--> black
    def __init__(self, key):        #self references the current instance of this class
        self.key=key                #needs a key to be initialized
        self.parent = None
        self.right=None
        self.left=None
        self.color=0
    def __str__(self):
        if(self.color==0):
            color = "Red"
        else:
            color = "Black"
        if self.parent is None:
            msg = ("Key: {}\nColor: {}\nLeft: {}\nRight: {}\n"
                .format(
                self.key,
                color,
                self.left.key,
                self.right.key,
            ))
        else:
            msg = ("Key: {}\nColor: {}\nLeft: {}\nRight: {}\nParent: {}\n"
                .format(
                self.key,
                color,
                self.left.key,
                self.right.key,
                self.parent.key,
            ))
        if self.parent is None:
            msg = "This node is the Root\n" + msg
        return msg

class RedBlackTree:
    def __init__(self):
        self.nil=Node(0)
        self.nil.color = 1                  #the root and the nil are black
        self.nil.left=None
        self.nil.right=None
        self.root = self.nil
        self.number_of_nodes= 0
    def search(self,key):
        node = self.root
        if(node.key==key):
            return True
        while (node != self.nil):  # as long as we didn't reach the end of the tree
            if node.key==key:
                return True
            elif key< node.key:
                node = node.left
            else:
                node = node.right
        return False
    def insert(self,key):
        newNode =Node(key)
        newNode.left=self.nil
        newNode.right=self.nil
        node = self.root
        parent=None                 #aka None aka nil

        while(node!=self.nil):      #as long as we didn't reach the end of the tree
            parent = node
            if newNode.key <node.key:
                node = node.left
            else:
                node = node.right
        newNode.parent= parent
        if parent == None:          #if the inserted node is the first node
            newNode.color =1
            self.root=newNode
            self.number_of_nodes = self.number_of_nodes + 1
            return
        elif newNode.key <parent.key:
            parent.left=newNode
        else:
            parent.right=newNode

        if newNode.parent.parent == None:       #if the inserted node is the second one
            self.number_of_nodes = self.number_of_nodes + 1
            return
        self.insertFix(newNode)
        self.number_of_nodes= self.number_of_nodes+1

    def insertFix(self, newNode):
        while newNode!=self.root and newNode.parent.color==0 :
            uncle = None
            parentIsLeft = False
            if newNode.parent == newNode.parent.parent.left:
                uncle = newNode.parent.parent.right
                parentIsLeft = True
            else:
                uncle = newNode.parent.parent.left
            #case 1: Uncle is red -> reverse colors of  uncle and parent with grandparent
            if uncle.color==0:
                newNode.parent.color=1
                uncle.color=1
                newNode.parent.parent.color=0
                newNode=newNode.parent.parent

            else:
                #case 2: uncle is
                # Left right condition
                if parentIsLeft and newNode == newNode.parent.right:
                    newNode = newNode.parent        #Take care as we made the new node the parent
                    self.leftRotate(newNode)
                #Right Left condition
                elif parentIsLeft ==False and newNode==newNode.parent.left:
                    newNode=newNode.parent
                    self.rightRotate(newNode)
                #left left condition
                if parentIsLeft:
                    newNode.parent.color=1          #the new parent
                    newNode.parent.parent.color= 0        #the new grandparent will be red
                    self.rightRotate(newNode.parent.parent)
                #right right condition
                else:
                    newNode.parent.color =1
                    newNode.parent.parent.color=0
                    self.leftRotate(newNode.parent.parent)
            self.root.color=1
    def leftRotate(self,node):
        """
         a          b
          \   =>   / \
           b      a   d
          /  \      \
        c     d      c
        """
        y = node.right
        node.right=y.left       #connect a to c
        if y.left!=self.nil:    #connect c to a
            y.left.parent=node

        y.parent=node.parent    #connect a's parent to b

        if node.parent==None:   #connect    b to a's parent
            self.root=y
        elif node == node.parent.left:
            node.parent.left=y
        else:
            node.parent.right= y

        y.left = node           #connect b to a
        node.parent = y         #connect a to b


    def rightRotate(self,node):
        """
         a                      b
       /   \        =>        /   \
      b                     c      a
    /   \                         /
   c     d                       d
        """
        y= node.left
        node.left = y.right     #connect a to d
        if y.right!=self.nil:   #connect d to a
            y.right.parent = node
        y.parent = node.parent  #connect a's parent to b

        if node.parent ==None:  #connect b parent to a's parent
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y

        y.right = node          #connect b to a
        node.parent = y         #connect a to b


    def printTreeSize(self):
        return self.number_of_nodes

    # Function to print
    def __printCall(self, node, indent, last):
        if node != self.nil:
            print(indent, end=' ')          #the default end characther is new line
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
    def heightOfTree(self,node,sum):
        if node is self.nil:
            return sum
        return max(self.heightOfTree(node.left, sum + 1), self.heightOfTree(node.right, sum + 1))


"""
tree= RedBlackTree()
tree.insert(10)
tree.insert(20)
tree.insert(50)
tree.insert(40)
tree.insert(30)
tree.insert(60)
tree.insert(70)
tree.insert(80)
tree.insert(90)
tree.insert(100)
print(tree.root)
tree.print_tree()
print(tree.heightOfTree(tree.root,0))
print(tree.number_of_nodes)
print(tree.search(91))
"""