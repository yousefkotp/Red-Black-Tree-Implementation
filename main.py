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
        msg = ("Key: {}\nColor: {}\nLeft: {}\nRight: {}\nParent: {}"
            .format(
            self.key,
            color,
            self.left.key,
            self.right.key,
            self.parent.key
        ))
        if self.parent.key is None:
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

    def insert(self,key):
        newNode =Node(key)
        newNode.parent=None
        newNode.left=self.nil
        newNode.right=self.nil

        node = self.root
        parent=None         #aka None aka nil
        while(node!=self.nil):  #as long as we didn't reach the end of the tree
            parent = node
            if newNode.key <node.key:
                node = node.left
            else:
                node = node.right
        newNode.parent= parent
        if parent == None:     #if the inserted node is the first node
            self.root=newNode
        elif newNode.key <parent.key:
            parent.left=newNode
        else:
            parent.right=newNode

        if node.parent==None:
            node.color=1
            return
        if node.parent.parent == None:
            return
        self.insertFix(newNode)
        self.number_of_nodes= self.number_of_nodes+1

    def insertFix(self, newNode):
        uncle = None
        parentIsLeft = False
        if newNode.parent==newNode.parent.parent.left:
            uncle = newNode.parent.parent.right
            parentIsLeft = True
        else:
            uncle = newNode.parent.parent.left
        while newNode.parent.color ==0:
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
                    newNode.parent.parent= 0        #the new grandparent will be red
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
        y=node.right
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



tree= RedBlackTree()
tree.insert(10)
tree.insert(20)
tree.insert(50)
tree.insert(40)
tree.insert(30)